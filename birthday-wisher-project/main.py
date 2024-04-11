import smtplib
import datetime as dt
import pandas
import random

email_data = pandas.read_csv("email_data.csv")
my_email_data = email_data.to_dict(orient="records")
email = my_email_data[0]["my_email"]
password = my_email_data[0]["password"]

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays_data.csv")

birthday_dict = {(record["month"], record["day"]): record for (index, record) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_{random.randint(1, 2)}.txt"
    with open(file_path) as letter:
        birthday_letter = letter.read()
        final_letter = birthday_letter.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:Happy Birthday!"
                                                                     f"\n\n{final_letter}")
