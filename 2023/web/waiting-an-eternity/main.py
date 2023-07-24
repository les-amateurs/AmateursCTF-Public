from flask import Flask, make_response, request
from time import time

app = Flask('app', static_url_path='')

@app.route('/secret-site')
def secret_site():
    secretcode = request.args.get('secretcode', '')
    if secretcode != "5770011ff65738feaf0c1d009caffb035651bb8a7e16799a433a301c0756003a":
        return make_response("you don't have the secret code", 401)
    ptime = request.cookies.get('time')
    if ptime == None:
        ptime = time()
        resp = make_response("welcome. please wait another eternity.")
        resp.set_cookie('time', str(ptime))
        return resp
    else:
        ptime = float(ptime)
    if time() - ptime < 1e308:
        return make_response(f"you have not waited an eternity. you have only waited {time() - ptime} seconds")
    else: 
        return "amateursCTF{im_g0iNg_2_s13Ep_foR_a_looo0ooO0oOooooOng_t1M3}"

@app.route('/')
def root():
    resp = make_response("just wait an eternity")
    resp.headers['Refresh'] = '1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000; url=/secret-site?secretcode=5770011ff65738feaf0c1d009caffb035651bb8a7e16799a433a301c0756003a'
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)