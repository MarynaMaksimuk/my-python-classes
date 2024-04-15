import smtplib
import datetime as dt
import random
import pandas


data = pandas.read_csv("email_data.csv")
my_data = data.to_dict(orient="records")
email = my_data[0]["my_email"]
password = my_data[0]["password"]


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 3:
    with open("quotes.txt") as data_file:
        data = data_file.readlines()
        today_quote = random.choice(data)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:Quote of the day"
                                                                                    f"\n\n{today_quote}")






