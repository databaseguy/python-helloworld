import requests
from datetime import datetime

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
