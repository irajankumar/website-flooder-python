import requests
from concurrent.futures import ThreadPoolExecutor
import time

def fetch(url):
    r = requests.get(url)
    print(r.status_code)
    return r.status_code


def main():
    url = 'https://www.example.com/index.php'
    counter = 0
    
    while True:
        counter +=1
        print("Round : ", counter)
        with ThreadPoolExecutor(max_workers=1000) as executor:
            executor.map(fetch,[url] * 1000)
            executor.shutdown(wait=True)
        print('\n')
        time.sleep(10)

main()