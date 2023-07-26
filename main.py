
import yagmail
import pandas
from news import NewsFeed
import datetime

from dotenv import load_dotenv
import os
load_dotenv()
# environment variables

EMAIL_ADDR=os.getenv("EMAIL_ADDR")
EMAIL_PW=os.getenv("EMAIL_PW")

smtp_server = "smtp.gmail.com"
smtp_port = 587
df = pandas.read_excel('people.xlsx')

def send_email(EMAIL_ADDR, EMAIL_PW, smtp_server, smtp_port, row):
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'], from_date=yesterday, to_date=today)

    email = yagmail.SMTP(user=EMAIL_ADDR, password=EMAIL_PW, host=smtp_server, port=smtp_port, smtp_starttls=True, smtp_ssl=False)
    email.send(to=row['Email'], 
                subject=f"Your {row['interest']} news for today!",
                contents=f"Hi {row['Name']}\n See what's on about {row['interest']} today. \n{news_feed.get()} \nRegan")

for index, row in df.iterrows():
    send_email(EMAIL_ADDR, EMAIL_PW, smtp_server, smtp_port, row)
