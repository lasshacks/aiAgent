import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from continue_add_numbers import add_numbers


WEB_DIRECTORY = Path(__file__).parent / "web"


class AdditionAppHandler(SimpleHTTPRequestHandler):
    """정적 화면과 덧셈 API를 제공하는 HTTP 요청 처리기입니다."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIRECTORY), **kwargs)

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/api/add":
            self.send_error(404, "Not Found")
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(content_length))
            first = float(payload["first"])
            second = float(payload["second"])
            result = add_numbers(first, second)
        except (KeyError, TypeError, ValueError, json.JSONDecodeError):
            self._send_json(400, {"error": "두 입력값에 올바른 숫자를 입력해주세요."})
            return

        self._send_json(200, {"result": result})

    def _send_json(self, status_code: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def create_server(port: int = 8000) -> ThreadingHTTPServer:
    """지정한 포트에서 실행할 덧셈 웹 서버를 생성합니다."""
    return ThreadingHTTPServer(("0.0.0.0", port), AdditionAppHandler)


if __name__ == "__main__":
    server = create_server()
    print("덧셈 앱 실행: http://localhost:8000")
    print("종료하려면 Ctrl+C를 누르세요.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n서버를 종료합니다.")
    finally:
        server.server_close()
