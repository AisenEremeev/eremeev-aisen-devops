import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def student():
    defaults = {'NAME': 'Aisen', 'SURNAME': 'Eremeev', 'GROUP': 'IT2-2314', 'ID': '37128'}
    return {key.lower(): os.getenv('STUDENT_' + key, value) for key, value in defaults.items()}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ('/', '/health'):
            self.send_error(404)
            return
        data = {'status': 'ok'} if self.path == '/health' else {
            'title': 'DevOps Student Application', **student(),
            'message': 'Application is running successfully!'}
        body = (json.dumps(data, indent=2) + '\n').encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    print(json.dumps(student()), flush=True)
    HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
