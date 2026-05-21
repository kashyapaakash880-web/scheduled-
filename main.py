import pandas
import smtplib
import datetime as dt
from random import choice
import os

PLACEHOLDER = "[NAME]"
##################### Hard Starting Project ######################
"""open the csv file to read and edit"""
with open("birthdays.csv") as file :
    file_data = file.read()

data = pandas.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")
# USED DICTIONARY COMPREHENSION
#dictionary for birthday
birthday_dict = { (data_row["day"],data_row["month"]):data_row for (index,data_row) in data.iterrows()}
"""create the current day and month """
current_day = dt.datetime.now()
tuple_date = (current_day.day, current_day.month)
"""name of birthday person  """
birth_person = birthday_dict[tuple_date]

if tuple_date in birthday_dict:

    with open("letter_templates/letter_1.txt","r") as file:
        file_content = file.read()
    with open("letter_templates/letter_2.txt","r") as file:
        file_content_1 = file.read()
    with open("letter_templates/letter_3.txt","r") as file:
        file_content_2 = file.read()

    random_letter = file_content , file_content_1 , file_content_2

    random_select = choice(random_letter)

    new_letter = random_select.replace(PLACEHOLDER,birth_person['name'])

    MY_EMAIL = os.environ.get(MY_EMAIL)
    MY_PASSWORD = os.environ.get(MY_PASSWORD)

    # connect to Gmail server
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # secure the connection
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birth_person['email'],
            msg=f"Subject: Happy Birthday Brother\n\n{new_letter}",
        )
else:
    print("no birthday sorry ")

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



