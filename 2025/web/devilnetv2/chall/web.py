#!/usr/bin/env python3
import base64, logging, sys, os, time
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from http.cookies import SimpleCookie


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


flag = os.getenv("FLAG", "amateursCTF{t3st_f14g}") # charset: a-z{}
binary_location = os.environ.get("CHROME_BIN", "/usr/bin/chromium")
service_location = os.environ.get("CHROMEDRIVER", "/usr/bin/chromedriver")

# Teemo website
template = """<html>
<head>
    <title>Teemo Scout</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Welcome to the Teemo Scout</h1>
    <p>Use this service to scout for Teemo's hidden zones.</p>
    <p>To scout, append <code>?content=your_content_here</code> to the URL.</p>
    <p>Example: <code>/scout?content=HelloTeemo</code></p>
    <p>Happy scouting!</p>
    <p>
    <flag>
    <replaceme>
    </p>
</body>
</html>
"""


class TeemoScoutHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        params = parse_qs(parsed_url.query)
        if path == '/bot':
            return self.handle_bot(params)

        parsed    = urlparse(self.path)
        content    = parse_qs(parsed.query).get('content', [""])[0]

        scout_out = 'deadbeef' + content
        if scout_out.count('\n') >= 5 or not all(x not in scout_out.lower() for x in ['stat', 'type','loc', 'ref']):
            scout_out = 'invalid content'

        self.server_version = f"TeemoNet/v2"
        self.sys_version    = f'{scout_out}'

        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')

        cookies = SimpleCookie(self.headers.get('Cookie', ''))
        stuff = cookies.get('FLAG', None)
        body = template.replace("<flag>", stuff.value if stuff else "")
        body = body.replace("<replaceme>", scout_out)
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body.encode())

    def handle_bot(self, params):
        print(f"[+] Bot requested to visit URL with params: {params}", file=sys.stderr)
        try:
            address = params.get('address', ['uhm'])[0]
            data = base64.b64decode(address).decode()
            
            url = f"http://127.0.0.1:9192/scout?content={data}"
            print(f"[+] Visiting {url}", file=sys.stderr)
            
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")  # helps in Docker
            options.binary_location = binary_location
            service = Service(service_location)
            driver = webdriver.Chrome(service=service, options=options)
            print("[-] Chrome WebDriver started", file=sys.stderr)
            
            driver.get('http://127.0.0.1:9192/void')
            driver.add_cookie({'name':'FLAG','value': flag})
            print(f"[-] Visiting URL {url}", file=sys.stderr)
            driver.get(url)
            driver.implicitly_wait(5)
            time.sleep(3)
            driver.quit()
            print(f"[-] Done visiting {url}", file=sys.stderr)

            self.send_response(302)
            self.send_header('Location', 'http://127.0.0.1:9192/')
            self.send_header('Content-Length','0')
            self.end_headers()
        except Exception as e:
            print(e, file=sys.stderr)
            self.send_response(400)
            self.send_header('Content-Length','0')
            self.end_headers()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    port = 9192
    logging.info(f"Teemo Scout server listening on {port}")
    HTTPServer(("0.0.0.0", port), TeemoScoutHandler).serve_forever()
