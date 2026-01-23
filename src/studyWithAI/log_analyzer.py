import os
from googletrans import Translator
import asyncio

# Initialize the Google Translator object
# 구글 번역기 객체를 초기화합니다.
translator = Translator()

# Define a list of keywords to search for in the log file
# 로그 파일에서 검색할 키워드 목록을 정의합니다. (Case-insensitive: 대소문자 구분 없음)
target_keywords = ["error", "warning", "unsatisfied", "failed"]

async def analyze_logs(file_path):
    # Extract the file name from the full path for display
    # 출력을 위해 전체 경로에서 파일 이름만 추출합니다.
    print(f"--- Analyzing Log File: {os.path.basename(file_path)} ---")

    try:
        # Open the file in 'read' mode with UTF-8 encoding
        # 파일을 UTF-8 인코딩의 '읽기' 모드로 엽니다.
        with open(file_path, "r", encoding="utf-8") as file:
            # Iterate through each line with its line number starting from 1
            # 1부터 시작하는 라인 번호와 함께 각 줄을 반복문으로 돕니다.
            for line_number, line in enumerate(file, start=1):
                # Check if 'any' of the keywords exist in the lowercase version of the line
                # 현재 줄을 소문자로 변환한 내용 중에 키워드가 '하나라도' 있는지 확인합니다.
                if any(word in line.lower() for word in target_keywords):
                    # Remove unnecessary whitespace from both ends
                    # 양 끝의 불필요한 공백과 줄바꿈을 제거합니다.
                    original_text = line.strip()
                    
                    # Translate the original text to Korean (dest="ko")
                    # 원문 텍스트를 한국어로 번역합니다.
                    translated_obj = await translator.translate(original_text, dest="ko")
                    translated_text = translated_obj.text
                    
                    print(f"[{line_number}] 원본:{original_text}")
                    print(f"     번역:{translated_text}")
                    print("-" * 50) # Visual separator for better readability

    # Exception handling for missing files
    # 파일을 찾을 수 없을 경우에 대한 예외 처리를 수행합니다.
    except FileNotFoundError:
        print(f"Error: The specified file was not found.")
    
    # Catch any other unexpected exceptions
    # 그 외 예상치 못한 모든 예외를 포착합니다.
    except Exception as e:
        print(f"An error occurred: {e}")

# Get the file path from the user through the console
# 콘솔을 통해 사용자로부터 파일 경로를 입력받습니다.
user_input = input("Please enter the full path of the log file: ")

# Execute the function with the provided input
# 제공된 입력값으로 함수를 실행합니다.
asyncio.run(analyze_logs(user_input))
