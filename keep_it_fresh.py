import requests
import schedule
import time

def ping():
    requests.get('http://localhost:5001/refresh')
    print('PING')

schedule.every(10).seconds.do(ping)

while True:
    schedule.run_pending()
    time.sleep(1)    