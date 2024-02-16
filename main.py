import requests
import time

def send_request(date):
    url = "https://app.humanwave.nl/contacts/*****/tasks-hours"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
    }
    body = f"date={date}&hours=%5B%7B%22allocation%22%3A%****%22%2C%22hours%22%3A%229%22%2C%22note%22%3A%22%22%7D%5D"

    response = requests.post(url, headers=headers, data=body)
    if response.ok:
        print(f"Request for date {date} was successful.")
    else:
        print(f"Request for date {date} failed with status: {response.status_code}")
    print(f"Response for date {date}:", response.text)

def delay(ms):
    time.sleep(ms / 1000)  # Convert milliseconds to seconds

def convert_to_full_date(input):
    year = "2024"  # Specify the year here
    day, month = input.split("-")
    return f"{year}-{month}-{day}"

# Example usage:
input_string = "05-02 06-02 07-02 06-02"
date_inputs = input_string.split(" ")
full_dates = [convert_to_full_date(date_input) for date_input in date_inputs]

def process_dates():
    for date in full_dates:
        send_request(date)
        delay(2000)  # Wait for 2 seconds

if __name__ == "__main__":
    process_dates()
