import re
from urllib.request import urlopen

url = "https://www.google.com"
with urlopen(url) as response:
    html = response.read().decode("utf-8", errors="ignore")

match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
print(match.group(1).strip() if match else "No title found")