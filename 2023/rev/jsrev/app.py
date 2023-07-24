from flask import Flask, render_template, send_from_directory, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('error.html')

# janky hack m8
allow_list = ['coords.json', 'collision-world.glb', 'main.css', 'main.js']
@app.route('/<path:path>')
def static_file(path):
    if path in allow_list:
        return send_from_directory('static', path)
    return redirect('/error')

if __name__ == '__main__':
    app.run(debug=True)
