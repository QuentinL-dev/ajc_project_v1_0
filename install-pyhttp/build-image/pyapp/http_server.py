#!/usr/bin/env python3

import os
import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler


class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = 'htdocs'
        return SimpleHTTPRequestHandler.do_GET(self)


class PythonHTTPServer:

    def __init__(self):
        self.port = 4443
        self.handler = MyHandler
        self.server = HTTPServer(("", self.port), self.handler)

    def check_SSL_certificate(self):
        if os.path.isfile('./key.pem') and os.path.isfile('./cert.pem'):
            return True
        return False

    def generate_SSL_certificate(self):
        os.system('openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365')

    def run(self):
        if not self.check_SSL_certificate():
            self.generate_SSL_certificate()
        self.server.socket = ssl.wrap_socket(self.server.socket, keyfile="key.pem", certfile="cert.pem", server_side=True)
        self.server.serve_forever()


if __name__ == '__main__':
    httpd = PythonHTTPServer
    httpd.run()
