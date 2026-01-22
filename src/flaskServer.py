from flask import Flask, render_template, request
import psycopg2
from datetime import datetime

app = Flask(__name__, template_folder='../templates')

# DB 연결 설정 함수
def get_db_connection():
    return psycopg2.connect(
        host="localhost", # 도커 외부(로컬)에서 접속하므로 localhost
        database="mydb",
        user="user",
        password="password"
    )

@app.route('/')
def index():
    # 1. DB에 접속하여 로그 남기기
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # 테이블이 없으면 생성
        cur.execute("""
            CREATE TABLE IF NOT EXISTS access_logs (
                path TEXT,
                access_time TIMESTAMP
            );
        """)
        
        # 로그 삽입 (request.path를 통해 현재 경로 파악)
        cur.execute("INSERT INTO access_logs (path, access_time) VALUES (%s, %s)", 
                    (request.path, datetime.now()))
        
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"DB Error: {e}")

    # 2. templates/index.html 파일을 읽어서 응답
    return render_template('index.html')

@app.route('/testMain')
def testMain():
    return render_template('testMain.html')

if __name__ == '__main__':
    # debug=True를 설정하면 코드를 수정할 때마다 서버가 자동으로 재시작됩니다.
    app.run(host='0.0.0.0', port=8000, debug=True)
