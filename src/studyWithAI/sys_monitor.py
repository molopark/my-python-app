import psutil
import smtplib
from email.mime.text import MIMEText
import datetime

# --- Configuration (Set your credentials here) ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "molopark@gmail.com"
SENDER_PASSWORD = "your_app_password" # Use App Password, not login password
RECEIVER_EMAIL = "molopark@gmail.com"
# --- End of Configuration ---

CPU_THRESHOLD = 80.0
MEM_THRESHOLD = 80.0

def send_alert_email(cpu_usage):
    """Sends an email notification when system is overloaded."""
    # Compose the email content in English
    subject = "[ALERT] System Overload Detected"
    body = f"""
    Dear Administrator,
    
    This is an automated alert from your System Monitor.
    The CPU usage has exceeded the threshold.
    
    - Current CPU Usage: {cpu_usage}%
    - Threshold: {CPU_THRESHOLD}%
    - Timestamp: {datetime.datetime.now()}
    
    Please check the server status immediately.
    """
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        # Connect to the server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls() # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print("Alert email has been sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def monitor_system():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        mem_percent = psutil.virtual_memory().percent

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] current CPU Usage: {cpu_percent}%, Memory Usage: {mem_percent}%")

        if cpu_percent > CPU_THRESHOLD or mem_percent > MEM_THRESHOLD:
            print(f"[{timestamp}] WARNING CPU Usage: {cpu_percent}%, Memory Usage: {mem_percent}%")
            send_alert_email(cpu_percent)

monitor_system()