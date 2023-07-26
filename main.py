import yagmail
import pandas
from news import NewsFeed

from dotenv import load_dotenv
import os
load_dotenv()
# environment variables

os.getenv("EMAIL_ADDR")
os.getenv("EMAIL_PW")


df = pandas.read_excel('people.xlsx')

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], from_date='2023-07-22', to_date='2023-07-24')

    email = yagmail.SMTP(user="EMAIL_ADDR", password="EMAIL_PW")
    email.send(to=row['Email'], 
                subject=f"Your {row['interest']} news for today!",
                contents=f"Hi {row['Name']}\n See what's on about {row['interest']} today. \n{news_feed.get()} \nRegan")

print(df)
