import schedule 
import requests

def task():
    requests.get("http://127.0.0.1:8000/sendNotification/")


schedule.every(1).minutes.do(task)

while True:
    schedule.run_pending()