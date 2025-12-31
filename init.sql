CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. 초기 데이터 삽입
--INSERT INTO users (username, email) VALUES 
--('admin', 'admin@example.com'),
--('testuser', 'test@example.com');
