# ls version simple

import http.server
import socketserver

port = 80
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", 80 ), Handler)

httpd.serve_forever()
