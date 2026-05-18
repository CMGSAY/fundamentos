from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        body = json.dumps(data).encode('utf-8')
        self.wfile.write(body)

    def do_GET(self):
        if self.path == '/':
            self.send_json({'message': 'Hola Mundo desde la raiz'})
        elif self.path == '/hello':
            self.send_json({'message': 'Hello World from /hello'})
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), MyHandler)
    print('Servidor HTTP escuchando en http://localhost:8080')
    server.serve_forever()