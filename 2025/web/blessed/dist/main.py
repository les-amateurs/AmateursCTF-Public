import flask
import re
import os
import urllib.parse
import threading

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

app = flask.Flask(__name__)


@app.route('/')
def index():
    query = flask.request.args.get('q')
    if query:
        if re.search(r's|r|n|htm|a', query, re.IGNORECASE): # s|r - scr/src, n - on, htm - html, a - data
            return '<h1>Invalid query</h1>'
        else:
            return f'<h1>{query}</h1>'
    else:
        return '<h1>Hello, World!</h1>'


#### The following does not have any intended vulnerabilities. ####

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if flask.request.method == 'GET':
      return '''
        <form action="/admin" method="post">
          Query: <input type="text" name="q">
          <input type="submit" value="Fetch">
        </form>
      '''
    
    content = flask.request.form.get('q')
    if not content:
      return "<h1>Error: No query provided</h1>"
    
    try:
      print(f'Visiting with content: {content}')
      url = f'http://localhost:8888/?q={urllib.parse.quote(content)}'
      visit_with_playwright(url)
      return "<h1>Admin visited your URL.</h1>"
    except PlaywrightTimeoutError:
      return "<h1>Error: Timed out fetching page</h1>"
    except Exception as e:
      return f"<h1>Error: {str(e)}</h1>"


def visit_with_playwright(url: str):
    def _visit(playwright):
        chromium = playwright.chromium
        launch_args = {
            "headless": True,
            "args": [ "--no-sandbox", 
                     "--disable-cache", 
                     "--disable-web-security",
                    ]
        }
        browser = chromium.launch(**launch_args)

        context = browser.new_context()
        page = context.new_page()

        page.goto(url, timeout=2000)
        page.wait_for_timeout(1000)

        browser.close()
    with sync_playwright() as playwright:
        _visit(playwright)



FLAG = os.environ.get("FLAG", "amateursCTF{t3st_f14g}")

csaw = flask.Flask("csaw")

@csaw.route('/flag')
def flag():
    return FLAG

@csaw.after_request
def add_cors(resp):
    return resp

def csaw_run():
    csaw.run(host='127.0.0.1', port=20070)


if __name__ == '__main__':
    threading.Thread(target=csaw_run, daemon=True).start()
    app.run(host='0.0.0.0', port=8888)
