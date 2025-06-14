import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

def check_website_performance(url):
    try:
        # Send a GET request to the website
        response = requests.get(url, timeout=10)

        # Measure response time
        response_time = response.elapsed.total_seconds()

        # Check the status code
        if response.status_code == 200:
            print(f"[{datetime.now()}] {url} is up. Response time: {response_time} seconds.")
        else:
            print(f"[{datetime.now()}] {url} is down. Status code: {response.status_code}.")
            return False, response_time

        return True, response_time

    except requests.exceptions.RequestException as e:
        # Handle exceptions like connection errors, timeouts, etc.
        print(f"[{datetime.now()}] Error checking {url}: {e}")
        return False, None

def send_email_alert(subject, body, to_email):
    from_email = 'your-email@example.com'
    password = 'your-email-password'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("Alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def monitor_websites(websites, threshold):
    for url in websites:
        is_up, response_time = check_website_performance(url)

        if not is_up or (response_time is not None and response_time > threshold):
            # Prepare email alert
            subject = f"Website Performance Alert: {url}"
            body = f"Website {url} is down or slow. Response time: {response_time} seconds."
            send_email_alert(subject, body, 'recipient-email@example.com')

websites_to_monitor = [
    'https://www.example.com',
    'https://www.another-example.com'
]

response_time_threshold = 2.0  # in seconds

monitor_websites(websites_to_monitor, response_time_threshold)
