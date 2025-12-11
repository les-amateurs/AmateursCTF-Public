#!/usr/bin/env bash

# no funny stuff.
# credit to pwn.college for this snippet
set -euo pipefail
exec 2>/dev/null
set -T
readonly BASH_SUBSHELL
trap '[[ $BASH_SUBSHELL -gt 0 ]] && exit' DEBUG

readonly SCREEN_WIDTH=16
readonly SCREEN_HEIGHT=8

snake_x=(0)
snake_y=(0)
food_x=0
food_y=0
uid=0

register() {
    uid=$RANDOM$RANDOM$RANDOM
    echo UID: $uid
    echo -n "Password: " 
    read input_passwd

    echo $uid >> /srv/app/data/uids.txt
    echo -n $input_passwd > /srv/app/data/passwd/$uid.txt
    echo Registered!
}

login() {
    echo -n "UID: "
    read input_uid
    echo -n "Password: " 
    read input_passwd

    ./login.py $input_uid $input_passwd
    local login_status=$?
    if [ $login_status -eq 0 ] || [ $login_status -eq 255 ]; then
        uid=$input_uid
    fi
    return $login_status
}

admin_menu() {
    while true; do
        echo
        echo ================================
        echo
        echo 🧸 Super Secret Admin Menu 🧸
        echo
        echo ================================
        echo
        echo Commands:
        echo "  view_users - view all registered users"
        echo "  flag       - get the flag"
        echo "  logout     - logout of admin menu"
        echo
        echo -n "> "
        read input

        case $input in
            view_users)
                cat /srv/app/data/uids.txt
                ;;
            flag)
                echo -n "Flag: "
                /readflag
                echo
                ;;
            logout)
                return 0
                ;;
            *)
                echo Invalid command
                ;;
        esac
    done
}

user_menu() {
    snake_x=($((RANDOM % SCREEN_WIDTH)))
    snake_y=($((RANDOM % SCREEN_HEIGHT)))
    spawn_food
    echo
    echo Commands:
    echo "  wasd - move"
    echo "  settings - user settings menu"
    draw_screen

    local last_move=s
    while true; do
        echo -n "> "
        read input

        if [ -z $input ]; then
            input=$last_move
        fi

        if [ $input = settings ]; then
            echo
            echo Commands:
            echo "  score  - view your last score"
            echo "  save   - save your current score"
            echo "  delete - delete your account"
            echo "  back   - return to game"
            echo "  logout - logout of user menu"
            echo
            echo -n "> "
            read input

            case $input in
                score)
                    echo -n "Your last score: "
                    cat /srv/app/data/score/$uid.txt 2>/dev/null || echo 0
                    ;;
                save)
                    local score=${#snake_x[@]}
                    echo $score > /srv/app/data/score/$uid.txt
                    echo Game saved. Your score of $score has been saved.
                    ;;
                delete)
                    rm -f /srv/app/data/passwd/$uid.txt
                    rm -f /srv/app/data/score/$uid.txt
                    sed -i "/^$uid$/d" /srv/app/data/uids.txt
                    echo Account deleted.
                    return 0
                    ;;
                logout)
                    local score=${#snake_x[@]}
                    echo $score > /srv/app/data/score/$uid.txt
                    echo Logged out. Your score of $score has been saved.
                    return 0
                    ;;
                back)
                    continue
                    ;;
                *)
                    echo Invalid command
                    continue
                    ;;
            esac
        fi

        local dx=0 dy=0
        case $input in
            w) dy=-1 ;;
            s) dy=1 ;;
            a) dx=-1 ;;
            d) dx=1 ;;
            *)
                continue
                ;;
        esac
        last_move=$input

        local new_x=$(( snake_x[0] + dx ))
        local new_y=$(( snake_y[0] + dy ))
        if [ $new_x -lt 0 ] || [ $new_x -ge $SCREEN_WIDTH ] || [ $new_y -lt 0 ] || [ $new_y -ge $SCREEN_HEIGHT ]; then
            game_over
            return 0
        fi

        local collision=false
        for ((i=0; i<${#snake_x[@]}; i++)); do
            if [ ${snake_x[i]} -eq $new_x ] && [ ${snake_y[i]} -eq $new_y ]; then
                collision=true
                break
            fi
        done
        if [ $collision = true ]; then
            game_over
            return 0
        fi

        snake_x=( $new_x ${snake_x[@]} )
        snake_y=( $new_y ${snake_y[@]} )

        if [ $new_x -eq $food_x ] && [ $new_y -eq $food_y ]; then
            if [ ${#snake_x[@]} -eq $((SCREEN_WIDTH * SCREEN_HEIGHT)) ]; then
                echo You win! Maximum score achieved!
                local score=${#snake_x[@]}
                echo $score > /srv/app/data/score/$uid.txt
                return 0
            fi
            spawn_food
        else
            unset snake_x[-1]
            unset snake_y[-1]
        fi

        draw_screen
    done
}

game_over() {
    local score=${#snake_x[@]}
    echo Game Over! Your score: $score
    echo $score > /srv/app/data/score/$uid.txt
}

spawn_food() {
    while true; do
        food_x=$((RANDOM % SCREEN_WIDTH))
        food_y=$((RANDOM % SCREEN_HEIGHT))
        local collision=false
        for ((i=0; i<${#snake_x[@]}; i++)); do
            if [ ${snake_x[i]} -eq $food_x ] && [ ${snake_y[i]} -eq $food_y ]; then
                collision=true
                break
            fi
        done
        if [ $collision = false ]; then
            break
        fi
    done
}

draw_screen() {
    # echo -e "\x1b[2J\x1b[H"
    # poor mans screen clearing
    echo
    local screen=()
    for ((y=0; y<SCREEN_HEIGHT; y++)); do
        local row=""
        for ((x=0; x<SCREEN_WIDTH; x++)); do
            row+=.
        done
        screen+=($row)
    done

    for ((i=0; i<${#snake_x[@]}; i++)); do
        local x=${snake_x[i]}
        local y=${snake_y[i]}
        local row=${screen[y]}
        if [ $i -eq 0 ]; then
            screen[y]=${row:0:x}@${row:x+1}
        else
            screen[y]=${row:0:x}O${row:x+1}
        fi
    done

    local row=${screen[food_y]}
    screen[food_y]=${row:0:food_x}X${row:food_x+1}

    for row in ${screen[@]}; do
        echo $row
    done
}

while true; do
    echo
    echo ================================
    echo
    echo 🧸 Welcome to the Bear Snake Game! 🧸
    echo
    echo ================================
    echo
    echo Commands:
    echo "  register - create a new account"
    echo "  login    - login to your account"
    echo "  exit     - exit the game"
    echo
    echo -n "> "
    read input

    case $input in
        register)
            register
            user_menu
            ;;
        login)
            set +e
            login
            login_status=$?
            set -e
            if [ $login_status -eq 0 ]; then
                user_menu
            elif [ $login_status -eq 255 ]; then
                admin_menu
            else
                echo Login failed.
            fi
            ;;
        exit)
            echo Goodbye!
            exit 0
            ;;
        *)
            echo Invalid command
            ;;
    esac
done
