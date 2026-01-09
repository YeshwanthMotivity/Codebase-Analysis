import requests

url = "http://127.0.0.1:5001/"
try:
    print(f"Testing connection to {url}...")
    # Send a dummy file/request
    files = {'file': ('test.txt', 'hello world')}
    data = {'question': 'test'}
    response = requests.post(url, files=files, data=data, timeout=5)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Connection failed: {e}")
