from flask import Flask, render_template, request, redirect, url_for
import os
from Crypto.Util.number import bytes_to_long

app = Flask(__name__)
password = "this isn't the real password (it's redacted)"

def generate_note_id():
    return bytes_to_long(os.urandom(8))

notes_db = {generate_note_id():password}

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
    app.run(host='::', port=8000)
