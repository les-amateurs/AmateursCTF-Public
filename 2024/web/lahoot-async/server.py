from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form

import os

from pydantic import BaseModel

import fastapi
print("Fastapi version",fastapi.__version__)

import config

import secrets

import copy

import asyncio

from collections import defaultdict

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

leaderboard = defaultdict(lambda: 0)
username_to_token = dict()
session_states = dict()

def generate_leaderboard_list():
    return sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

def make_error_response(message):
    redirect_response = RedirectResponse(url="/", status_code = 303)
    redirect_response.set_cookie(key="error", value=message)
    return redirect_response

def make_leaderboard_redirect():
    redirect_response = RedirectResponse(url="/leaderboard", status_code = 303)
    redirect_response.set_cookie(key="redirected", value="1")
    return redirect_response

def secret_shuffle(original_list):
    queue = original_list.copy()
    shuffled = []
    while queue:
        el = secrets.choice(queue)
        shuffled.append(el)
        queue.pop(queue.index(el))
    return shuffled

def pick_question(session_state):
    session_state["current_question_index"] += 1
    if session_state["current_question_index"] > config.DESIRED_QUESTIONS:
        session_state["expired"] = True
        return session_state
    question_sets = config.choose_question_sets(session_state["current_question_index"])
    questions = config.get_questions(question_sets)
    # pick the question
    question = None
    while True:
        question = copy.deepcopy(secrets.choice(questions))
        if question["id"] not in session_state["seen_ids"]:
            session_state["seen_ids"].add(question["id"])
            break
    question["answers"] = secret_shuffle(secret_shuffle(question["answers"]))
    session_state["current_question"] = question
    return session_state

def initalize_session(username):
    token = secrets.token_hex(16)
    username_to_token[username] = token
    leaderboard[username] = 0
    session_states[token] = {
        "current_question_index": 0,
        "current_question": None,
        "previous_question_state": [],
        "seen_ids": set(),
        "username": username,
        "expired": False,
        "answered_questions": []
    }
    session_states[token] = pick_question(session_states[token])
    return token

def load_details(request: Request):
    if request.cookies.get("session", None) is None or not request.cookies.get("session", None) in session_states:
        return None
    return session_states[request.cookies.get("session", None)]

# class SessionStart(BaseModel):
#     username: str

@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    resp = templates.TemplateResponse(
        request = request, name="home.html", context = {
            "leaderboard": generate_leaderboard_list(),
            "brand": config.BRAND,
            "error": request.cookies.get("error", None),
            "session_state": load_details(request)
        }
    )
    
    if request.cookies.get("error", None):
        resp.delete_cookie("error")
    
    return resp

def get_endgame_data(session_state):
    data = {
        "message": "You did great! However, there's more accuracy to be gained. Keep going for the flag!"
    }
    
    correct = 0
    for question in session_state["answered_questions"]:
        if question["correct"]:
            correct += 1
            
    data["correct_count"] = correct
    data["accuracy"] = 100 * (correct / len(session_state["answered_questions"]))
    
    if correct == config.DESIRED_QUESTIONS:
        data["message"] = "Congratulations! You've achieved the flag! " + os.getenv("FLAG", "FLAG{this_is_a_fake_flag}")
    
    # TODO: Check for flag conditions
    
    return data

def make_endgame_response(request: Request, session_state):
    return templates.TemplateResponse(
        request=request, name="endgame.html", context={
            "session_state": session_state,
            "leaderboard": generate_leaderboard_list(),
            "brand": config.BRAND,
            "endgame_data": get_endgame_data(session_state)
        }
    )

questions_by_id = dict()
for question in config.get_all_questions():
    questions_by_id[question["id"]] = question

@app.get("/api/question/{question_id}")
def get_question(request: Request, question_id: str):
    return questions_by_id[question_id]

@app.post("/session", response_class=RedirectResponse)
async def start_session(request: Request, username: str = Form()):
    redirect = RedirectResponse(url = "/question", status_code = 303)
    
    if username in username_to_token:
        # token already used
        return make_error_response("Username already in use. If you own this account, you might be able to regain control of it by recovering it's token.")
    
    if len(username) > 16:
        return make_error_response("Username exceeds a length of 16. Please choose a shorter username to reduce spam.")

    if len(username) < 3:
        return make_error_response("Username needs at least 3 characters. Please choose a longer username to reduce spam.")
    
    redirect.set_cookie("session", initalize_session(username))
    return redirect


# TODO: logout function

@app.get("/leaderboard", response_class=HTMLResponse)
async def get_root(request: Request):
    session_state = load_details(request)
    if session_state and session_state["expired"]:
        return make_endgame_response(request, session_state)
    resp = templates.TemplateResponse(
        request = request, name="leaderboard.html", context = {
            "leaderboard": generate_leaderboard_list(),
            "brand": config.BRAND,
            "session_state": session_state
        }
    )
    
    if request.cookies.get("redirected", None):
        resp.delete_cookie("redirected")
    
    return resp

@app.get("/question", response_class=HTMLResponse)
async def get_next_question(request: Request):
    if not load_details(request):
        return make_error_response("Invalid session.")
    session_state = load_details(request)
    if session_state["expired"]:
        return make_leaderboard_redirect()
    return templates.TemplateResponse(
        request=request, name="question.html", context={
            "session_state": session_state,
            "is_new": False,
            "total": config.DESIRED_QUESTIONS
        }
    )
    
@app.post("/question", response_class=HTMLResponse)
async def get_next_question(request: Request, answer: str = Form()):
    if not load_details(request):
        return make_error_response("Invalid session.")
    # process question
    session_state = load_details(request)
    if session_state["expired"]:
        return make_leaderboard_redirect()
    
    is_correct = session_state["current_question"]["correctAnswer"] == answer
    previous_question = session_state["current_question"]
    previous_question["correct"] = is_correct
    session_state["answered_questions"].append(previous_question)
    if is_correct:
        leaderboard[session_state["username"]] += 1
    
    pick_question(session_state)
    
    if session_state["expired"]:
        return make_leaderboard_redirect()
    
    return templates.TemplateResponse(
        request=request, name="question.html", context={
            "session_state": load_details(request),
            "previous_correct": is_correct,
            "previous_question": previous_question,
            "is_new": True,
            "total": config.DESIRED_QUESTIONS
        }
    )
    
