defmodule TfsnWeb.ProfileController do
  use TfsnWeb, :controller

  alias Tfsn.Accounts

  action_fallback TfsnWeb.FallbackController

  def feed(conn, %{"username" => username}) do
    case Accounts.get_user_by_username(username) do
      nil -> render(conn, :not_found)
      user -> render(conn, :feed, posts: Accounts.get_posts(user), user: user)
    end
  end

  def following(conn, params = %{"username" => username}) do
    sort = Map.get(params, "sort", "username")

    case Accounts.get_user_by_username(username) do
      nil ->
        render(conn, :not_found)

      user ->
        render(conn, :following,
          following: Accounts.get_following(user, &Map.get(&1, String.to_atom(sort))),
          user: user
        )
    end
  end

  def followers(conn, params = %{"username" => username}) do
    sort = Map.get(params, "sort", "username")

    case Accounts.get_user_by_username(username) do
      nil ->
        render(conn, :not_found)

      user ->
        render(conn, :followers,
          followers: Accounts.get_followers(user, &Map.get(&1, String.to_atom(sort))),
          user: user
        )
    end
  end

  def follow(conn, %{"username" => username}) do
    case Accounts.get_user_by_username(username) do
      nil ->
        render(conn, :not_found)

      other ->
        Accounts.follow(conn.assigns.current_user, other)

        conn
        |> put_status(302)
        |> put_flash(:info, "Successfuly followed #{username}")
        |> put_resp_header("location", ~p"/@/#{username}")
        |> redirect(to: ~p"/@/#{username}")
    end
  end

  def unfollow(conn, %{"username" => username}) do
    case Accounts.get_user_by_username(username) do
      nil ->
        render(conn, :not_found)

      other ->
        Accounts.unfollow(conn.assigns.current_user, other)

        conn
        |> put_status(302)
        |> put_flash(:info, "Successfuly unfollowed #{username}")
        |> put_resp_header("location", ~p"/@/#{username}")
        |> redirect(to: ~p"/@/#{username}")
    end
  end
end
