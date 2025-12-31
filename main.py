import psycopg2
from datetime import datetime

def run_example():
    try:
        # DB 연결 (docker-compose의 network_mode 덕분에 localhost 사용 가능)
        conn = psycopg2.connect(
            host="localhost", database="mydb", 
            user="user", password="password"
        )
        cur = conn.cursor()

        # 1. 테이블 생성 (sample_data: columndata, 생성일자)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sample_data (
                columndata TEXT,
                created_at TIMESTAMP
            );
        """)

        # 2. 데이터 삽입
        cur.execute("INSERT INTO sample_data (columndata, created_at) VALUES (%s, %s)", 
                    ("Docker 15 Test Data", datetime.now()))
        
        conn.commit()

        # 3. 데이터 조회
        cur.execute("SELECT * FROM sample_data;")
        for row in cur.fetchall():
            print(f"데이터: {row[0]} | 생성일: {row[1]}")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    run_example()
    