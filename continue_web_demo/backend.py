import math
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


PORT = 8001
STATIC_DIRECTORY = Path(__file__).parent / "static"


class MultiplyHandler(SimpleHTTPRequestHandler):
    """정적 화면과 곱셈 API를 함께 제공하는 요청 처리기입니다."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIRECTORY), **kwargs)

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/multiply":
            self.send_error(404, "Not Found")
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            form_data = parse_qs(self.rfile.read(content_length).decode("utf-8"))
            num1 = float(form_data["num1"][0])
            num2 = float(form_data["num2"][0])
            if not (math.isfinite(num1) and math.isfinite(num2)):
                raise ValueError
        except (KeyError, IndexError, TypeError, ValueError, UnicodeDecodeError):
            self._send_text(400, "올바른 숫자 두 개를 입력해주세요.")
            return

        result = num1 * num2
        self._send_text(200, f"Result: {self._format_number(num1)} × "
                             f"{self._format_number(num2)} = "
                             f"{self._format_number(result)}")

    def _send_text(self, status_code: int, message: str) -> None:
        body = message.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    @staticmethod
    def _format_number(value: float) -> str:
        return str(int(value)) if value.is_integer() else str(value)


def create_server(port: int = PORT) -> ThreadingHTTPServer:
    """지정한 포트에서 실행할 곱셈 웹 서버를 생성합니다."""
    return ThreadingHTTPServer(("0.0.0.0", port), MultiplyHandler)


def main() -> None:
    with create_server() as server:
        print(f"곱셈 앱 실행: http://localhost:{PORT}")
        print("종료하려면 Ctrl+C를 누르세요.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n서버를 종료합니다.")


if __name__ == "__main__":
    main()
