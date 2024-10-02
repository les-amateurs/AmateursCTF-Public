from flask import Flask, render_template, request, redirect, url_for
import os
from Crypto.Util.number import *
import random

app = Flask(__name__)

lcg_seed = random.getrandbits(64)
lcg_a = random.getrandbits(64)
lcg_c = random.getrandbits(64)
lcg_m = getPrime(64)

def generate_note_id():
    global lcg_seed
    lcg_seed = (lcg_a * lcg_seed + lcg_c) % lcg_m
    return lcg_seed

notes_db = {generate_note_id():open('password.txt').read()}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_note', methods=['POST'])
def add_note():
    note_id = generate_note_id()
    note = request.form.get('note')
    notes_db[note_id] = note
    return redirect(url_for('view_note', note_id=note_id))

@app.route('/view_note/<int:note_id>')
def view_note(note_id):
    note = notes_db.get(note_id, "Note not found")
    return render_template('view_note.html', note=note)


if __name__ == '__main__':
    app.run(host="::", port=8000)
