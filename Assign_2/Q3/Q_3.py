import requests
import sys

def send_request(url):
    response = requests.get(url)
    return response

if __name__ == "__main__":
    url = sys.argv[1]
    response = send_request(url)
    print(f"Response from {url}:\n{response.text}")
