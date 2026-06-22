import http.server
import socketserver

PORT = 8000
class MultiplyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Result: 5 * 3 = 15")

def main():
    server = socketserver.TCPServer(('localhost', PORT), MultiplyHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()