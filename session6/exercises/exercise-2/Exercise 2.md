### Exercise 2

**Extract currency conversions from the `api.frankfurter.app`.**

* Using a serial programming approach, use the following scripts to collect data from an API.
* Then, use `Threads` or the  `ThreadPoolExecutor`  to fetch data in parallel.
* Compare the time taken for both tasks.

**Supporting material.**

You can use the following scripts as your starting point. 

* Assume your task includes the following conversions. You can copy these values directly from here.

```
12, GBP, USD
15, GBP, USD
11, EUR, USD
13, GBP, USD
10, EUR, USD
14, GBP, USD
15, GBP, EUR
18, GBP, USD
11, EUR, USD
19, USD, GBP
```

* Store the data as a list of tuples and use the following code to extract the data. The following script shows the unpacking of an example input of the tuple values.

```python
# Define a list of tuples containing currency conversion data
data = [
    (12, 'GBP', 'USD'), 
    (15, 'GBP', 'USD'), 
    (11, 'EUR', 'USD')
]

# Iterate over each tuple in the list
for record in data:
    # Unpack the tuple into amount, from_currency, and to_currency
    amount, from_currency, to_currency = record
    
    # Print the unpacked values
    print(amount, from_currency, to_currency)
```

> The output looks like this:
>
> ```
> 12 GBP USD
> 15 GBP USD
> 11 EUR USD
> ```

* Study and run the following script, which opens a `txt` file in Python and reads it line by line.

```python
import requests

# Define the amount to be converted
amount = 10

# Define the currency to convert from
from_currency = "EUR"

# Define the currency to convert to
to_currency = "GBP"

# Construct the API URL with the defined parameters
url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

# Send a GET request to the API
response = requests.get(url)

# Parse the JSON response from the API
data = response.json()

# Extract the exchange rate for the target currency
rate = data['rates'][to_currency]

# Return the formatted conversion result
print(f"{amount} {from_currency} = {rate} {to_currency}")
```

> [!NOTE]
>
> The provided solutions extend this exercise by using a file to load the conversions.
>

