from flask import Flask, request, make_response


app = Flask(__name__)

@app.route("/")
def home():
    res = make_response()
    token = request.cookies.get("token")
    if token == None:
        default_flag = "amateursCTF{fake_flag}"
        res.set_cookie("token", default_flag)
        token = default_flag
    code = request.args.get("code", "")
    res.set_data(f"""<html>
    <head>
        <meta http-equiv="Content-Security-Policy" content="script-src 'none'; style-src 'unsafe-inline'">
    </head>
    <body>
        <h1>time to cause a ruckus</h1>
        <form id="form">
			<input type="text" name="code"/>
			<br>
            <input type="submit" value="lets go" />
		</form>
        <div id="result">
            <input type=hidden value={token} />
            {code}
        </div>
    </body>
    </html>""")
    return res

app.run()
