from datetime import datetime

def calculate_first_half_dates():
    today = datetime.today()
    if today.day >= 16:
        start_date = today.replace(day=1)
        end_date = today.replace(day=15)
        return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
    else:
        return None

# Example usage:
result = calculate_first_half_dates()
if result:
    print(f"Start Date: {result[0]}, End Date: {result[1]}")
else:
    print("Today's date is not in the second half of the month.")