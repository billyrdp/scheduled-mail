import pandas
import datetime as dt
import random
import smtplib
import os
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
today_tuple = (now.month, now.day)
birthday_dict = {(data_row.month,data_row.day):data_row for (index,data_row) in data.iterrows()}
print(birthday_dict)
print(today_tuple)
if today_tuple in birthday_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter = file.read()
        birthday_letter = letter.replace("[NAME]", data.name[1])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="silittletimmy@yahoo.com",
                            msg=f"Subject: Birthday Wish\n\n{birthday_letter}")







