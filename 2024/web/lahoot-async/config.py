import os, json

def load_set(filename, category = None):
    with open(filename, "r") as f:
        questions = json.load(f)
        if category:
            for question in questions:
                question["category"] = category
        return questions

import secrets
def load_set_augment(filename, category = None):
    questions = load_set(filename, category)
    for question in questions:
        # change ids
        question["id"] = secrets.token_urlsafe(32)
    return questions

BRAND = os.getenv('BRAND', 'Lahoot Async')

DESIRED_QUESTIONS = 200

QUESTION_SETS = {
#    "main": load_set("questions.json")
    "genshin": load_set("question_sets/genshin.json", "Genshin Impact"), # here comes cringe
    "hsr": load_set("question_sets/hsr.json", "Honkai Star Rail"),
    "league": load_set("question_sets/league.json", "League of Legends and Riot Games"),
    "impossible": load_set("question_sets/impossible.json", "Impossible") + load_set_augment("question_sets/impossible.json", "Impossible") + load_set_augment("question_sets/impossible.json", "Impossible")+ load_set_augment("question_sets/impossible.json", "Impossible") + load_set_augment("question_sets/impossible.json", "Impossible")
}

def choose_question_sets(step):
    if step <= 80:
        return ["genshin", "hsr"]
    elif step <= 120:
        return ["league"]
    elif step <= 150:
        # culmination
        return ["league","hsr","genshin","impossible"]
    else:
        return ["impossible"]
    
def get_questions(sets):
    questions = []
    for set_name in sets:
        questions.extend(QUESTION_SETS[set_name])
    return questions

def get_all_questions():
    questions = []
    for set_name in QUESTION_SETS:
        questions.extend(QUESTION_SETS[set_name])
    return questions

if __name__ == "__main__":
    print("Config OK")
    print("Got",len(get_all_questions()), " questions")