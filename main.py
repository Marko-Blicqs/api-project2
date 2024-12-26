import requests as rq
import sent_email as email
from datetime import datetime

API_KEY = "9cc06c3e03ed48f1aa1ea7da8e7e2016"
topic = input("choose a topic: ")
url = "https://newsapi.org/v2/everything?" \
           f"q={topic}" \
           "&language=en" \
           "&from=2024-11-26" \
           "&sortBy=publishedAt" \
           "&pageSize=20" \
           f"&apiKey={API_KEY}"

now = datetime.now().strftime("%Y_%m_%d_%H%M%S")
subject = f"News ({topic.title()}): {now}"

request = rq.get(url)
content = request.json()

message = []

for i, article in enumerate(content["articles"]):
    message.append(f"{i+1}) Title: {article['title']} \nURL: {article['url']}, \nDescription: {article['description']}\n\n")

str_msg = ''.join(message)

email.send_email(sender="user@example.com", message=str_msg, subject=subject)

print(f"type: {type(message)}")
print(str_msg)
