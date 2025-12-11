import logging
from http.server import ThreadingHTTPServer
from web import TeemoScoutHandler

# Teemo Scout CSP enforcement policy
CSP_POLICY = "default-src 'none'; script-src 'none'; child-src 'none'; connect-src 'none'; frame-src 'none'; frame-ancestors 'none'; img-src 'none'; font-src 'none'; manifest-src 'none'; media-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; plugin-types 'none'; sandbox 'none'; report-to 'none'; worker-src 'none'; prefetch-src 'none'; navigate-to 'none';"

class ScoutCSPHandler(TeemoScoutHandler):
    def send_response(self, code, message=None):
        self.send_response_only(code, message)
        self.send_header('Content-Security-Policy', CSP_POLICY)
        self.send_header('Server', self.version_string())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    port = 9192
    logging.info(f"Teemo Scout CSP server listening on {port}")
    server = ThreadingHTTPServer(("0.0.0.0", port), ScoutCSPHandler)
    server.serve_forever()