from flask import Flask, render_template, request, send_from_directory
from nanoid import generate
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/render", methods=['POST'])
def render():
    if request.method == 'POST':
        # Get the data from the POST request.
        latex = request.json['latex']
        if len(latex) > (1024 * 1024 * 5):
            return "A pro license of Latek is required to render large documents."
        docID = generate(size = 16)
        print(docID, " processing size ",len(latex))
        tex_filepath = "/app/inputs/" + docID + ".tex"
        with open(tex_filepath, "w") as f:
            f.write(latex)
        # Run the command and get the output.
        subprocess.run(["pdflatex","-output-directory=/app/documents","-output-format=pdf","-no-shell-escape",tex_filepath], cwd = "/app/inputs", stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL, stdin = subprocess.DEVNULL)
        return {
            "id": docID,
            "path": "/document/" + docID + ".pdf"
        }

@app.route('/document/<path:path>')
def send_report(path):
    return send_from_directory('documents', path)  

@app.route('/source/<path:path>')
def send_source(path):
    return send_from_directory('inputs', path)      

if __name__ == '__main__':
    app.run(host='0.0.0.0')