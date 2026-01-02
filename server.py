from http.server import HTTPServer, BaseHTTPRequestHandler
import psycopg2
from datetime import datetime

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 정적 파일(이미지, css, js 등) 및 크롬 개발자 도구 요청은 로그 남기지 않음
        if not self.path.endswith(('.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.ico')) \
           and self.path != '/.well-known/appspecific/com.chrome.devtools.json':
            # DB에 접속하여 로그 남기기
            try:
                conn = psycopg2.connect(
                    host="localhost", database="mydb", 
                    user="user", password="password"
                )
                cur = conn.cursor()
                # 로그 테이블이 없으면 생성
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS access_logs (
                        path TEXT,
                        access_time TIMESTAMP
                    );
                """)
                # 현재 경로와 시간 저장
                cur.execute("INSERT INTO access_logs (path, access_time) VALUES (%s, %s)", 
                            (self.path, datetime.now()))
                conn.commit()
                cur.close()
                conn.close()
            except Exception as e:
                print(f"DB Error: {e}")

        # 응답 코드 200 (성공) 설정
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        # 클라이언트에 보낼 메시지 작성
        self.wfile.write(b"<h1>Hello!</h1><p>This is a simple server running with standard Python libraries.</p>")

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()