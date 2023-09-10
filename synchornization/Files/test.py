import requests
from timer import timer


url = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


@timer(1, 1)
def main():
    with requests.Session() as session:  # Corrected line
        for _ in range(20):
            fetch(session, url)
