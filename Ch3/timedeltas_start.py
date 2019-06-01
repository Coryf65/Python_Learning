#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
# using a new import! a time delta is a span of time
from datetime import timedelta

# construct a basic timedelta and print it
print("using a timedelta...\n")
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
print("\nusing a timedelta...\n")
now = datetime.now()
print("today is: ", str(now))


# print today's date one year from now
print("one year from now will be: " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("in 2 days and 3 weeks it will be: " + str(now + timedelta(days=2, weeks=3)))


# calculate the date 1 week ago, formatted as a string\
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("one week ago it was: " + s)


### How many days until April Fools' Day?
today = date.today()
# setting up the day it should be on 2020 4 1
april_fools_day = date(today.year, 4, 1)
# check if it has passed already!
# use date comparison to see if April Fool's has already gone for this year
if april_fools_day < today:
    print("April Fool's day already went by %d days ago" % ((today - april_fools_day).days))
    # if it has, use the replace() function to get the date for next year
    april_fools_day = april_fools_day.replace(year = today.year + 1)

# Now calculate the amount of time until April Fool's Day  
time_to_afd = april_fools_day - today
print("It's just", time_to_afd.days, "days until April Fool's Day!")

