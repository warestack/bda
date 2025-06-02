import threading
import requests

# Create a semaphore with a count of 3 to limit concurrent connections
connection_semaphore = threading.Semaphore(3)

def fetch_currency_conversion(data):
    amount, from_currency, to_currency = data
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

    # Acquire the semaphore before making the API request
    connection_semaphore.acquire()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rate = data['rates'][to_currency]
            return f"{amount} {from_currency} = {rate} {to_currency}"
        else:
            return "Failed to fetch data from API"
    finally:
        # Release the semaphore after the API request is done
        connection_semaphore.release()

# Function to run the fetch_currency_conversion in a thread
def thread_function(data):
    result = fetch_currency_conversion(data)
    print(result)

# List of currency conversion data (amount, from_currency, to_currency)
conversion_requests = [
    (100, "USD", "EUR"),
    (200, "EUR", "GBP"),
    (300, "GBP", "USD"),
    (150, "USD", "JPY"),
    (250, "JPY", "INR"),
    (350, "INR", "CNY"),
    (400, "CNY", "AUD"),
    (500, "AUD", "CAD"),
    (600, "CAD", "CHF"),
    (700, "CHF", "USD")
]

# Create and start threads
threads = []
for request in conversion_requests:
    thread = threading.Thread(target=thread_function, args=(request,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All currency conversions have been fetched.")
