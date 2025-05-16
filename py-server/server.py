from http.server import BaseHTTPRequestHandler, HTTPServer

from reader import read_file
from pdf_reader import read_pdf_file

HOST_NAME = "localhost"
SERVER_PORT = 8081


class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/read":
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)

            res = read_file(body.decode("utf-8"))

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(res, "utf-8"))
        if self.path == "/readPDF":
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)

            res = read_pdf_file(body.decode("utf-8"))

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(res, "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")


if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, SERVER_PORT), Server)
    print(f"Python server started http://{HOST_NAME}:{SERVER_PORT}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Python server stopped.")
