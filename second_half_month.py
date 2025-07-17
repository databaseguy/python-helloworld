from datetime import datetime, timedelta

def calculate_second_half_previous_month():
    today = datetime.today()
    if today.day <= 15:
        # Calculate the last day of the previous month
        first_day_of_this_month = today.replace(day=1)
        last_day_of_previous_month = first_day_of_this_month - timedelta(days=1)
        
        # Calculate the 16th of the previous month
        sixteenth_of_previous_month = last_day_of_previous_month.replace(day=16)
        
        return sixteenth_of_previous_month.strftime("%Y-%m-%d"), last_day_of_previous_month.strftime("%Y-%m-%d")
    else:
        return None

# Example usage:
result = calculate_second_half_previous_month()
if result:
    print(f"Start Date: {result[0]}, End Date: {result[1]}")
else:
    print("Today's date is not in the first half of the month.")