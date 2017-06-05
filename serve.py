"""Serve content in the current directory over HTTPS."""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import sys

port = 4443

httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
try:
    httpd.socket = ssl.wrap_socket(httpd.socket,
        certfile=('my-ssl-cert.pem' if len(sys.argv) < 2 else sys.argv[1]),
        server_side=True)
except:
    print("Unable to serve over HTTPS!")
    print("Generate an SSL certificate (.pem file) using generate-pemfile.sh, or supply one as a command line arg.")
    raise

print("Go to: https://localhost:{}/".format(port))
print("[Ctrl+C to quit]")
httpd.serve_forever()
