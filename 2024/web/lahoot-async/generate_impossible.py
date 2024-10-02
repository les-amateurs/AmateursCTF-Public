import secrets
import json
impossible_questions = []
for i in range(10 * 1000):
    for a in ["0", "1", "2", "3", "4", "5", "6", "7"]:
        impossible_questions.append({
            "question": f"At an offset of {i} in decimal, the 3 left most bits of a random piece of memory decode to...",
            "answers": ["0", "1", "2", "3", "4", "5", "6", "7"],
            "correctAnswer": a,
            "id": secrets.token_hex(32)
        })
        
with open("question_sets/impossible.json", "w") as f:
    f.write(json.dumps(impossible_questions))
