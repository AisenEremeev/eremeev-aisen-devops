import json
import os
import threading
import unittest
from unittest.mock import patch
from urllib.request import urlopen
from http.server import HTTPServer
from main import Handler, student


class AppTests(unittest.TestCase):
    def test_environment(self):
        with patch.dict(os.environ, {'STUDENT_NAME': 'Test', 'STUDENT_ID': '42'}):
            self.assertEqual(student()['name'], 'Test')
            self.assertEqual(student()['id'], '42')

    def test_http(self):
        server = HTTPServer(('127.0.0.1', 0), Handler)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            base = f'http://127.0.0.1:{server.server_port}'
            with urlopen(base + '/health') as response:
                self.assertEqual(json.load(response), {'status': 'ok'})
            with urlopen(base) as response:
                self.assertEqual(json.load(response)['name'], student()['name'])
        finally:
            server.shutdown()
            server.server_close()
            worker.join()


if __name__ == '__main__':
    unittest.main()
