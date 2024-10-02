import sys
import secrets
import json

questions = []

for filepath in sys.argv[1:-1]:
    with open(filepath, "r") as f:
        for line in f:
            try:
                for question in json.loads(line):
                    question["id"] = secrets.token_hex(32) # setup an unique id for each question
                    questions.append(question)
                # questions.extend(json.loads(line))
            except:
                pass
            
with open(sys.argv[-1], "w") as f:
    json.dump(questions, f)
    
print(len(questions), " questions are in this combined set.")