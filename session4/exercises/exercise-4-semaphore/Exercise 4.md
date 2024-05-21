### Exercise 4

**Extract three currency conversions at a time using the `api.frankfurter.app`.**

* You can reuse the code developed in exercise 2.
* Use a `semaphore` of the `threading` library.

**Supporting material.**

You can use the following scripts as your starting point. 

* Here is the list of currency conversion data (`amount`, `from_currency`, `to_currency`)

```python
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
```

* Study and run the following script.

```python
# Create a semaphore with a count of 3 to limit concurrent connections
connection_semaphore = threading.Semaphore(3)
...

# Acquire the semaphore before making the API request
connection_semaphore.acquire()
... Send request for conversion...

# Release the semaphore after the API request is done
connection_semaphore.release()
```

