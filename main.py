import smtplib
import datetime as dt
import random

my_email = 'rhbanks@gmail.com'
password = 'Password'

current_time = dt.datetime.now()
# example   month = current_time.month
current_day = current_time.weekday()
print(current_day)

if current_day == 1:
    with open("quotes.txt") as data:
        data = data.readlines()
        daily_quote = random.choice(data)
        # print(daily_quote)

        # if you do not use close() as seen below
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rhbanks@aol.com",
            msg=daily_quote
        )

# creating a new smtp object, inside quotes is the server location
# connection = smtplib.SMTP("smtp.gmail.com")
# this makes your connection secure
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs='rhbanks@aol.com', msg='Subject:Hello\n\nThis is the body of my email.')
# connection.close()



