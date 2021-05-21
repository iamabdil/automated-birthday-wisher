import datetime as dt
import pandas as pd
import random
import smtplib
import os

EMAIL = os.environ['MY_EMAIL']
PASS = os.environ['MY_PASS']

now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=birthday_person.email,
                            msg=f"Subject:Happy Birthday!!, \n\n{contents}")





