#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
print("\ncreate a plain text calendar...\n")
cal = calendar.TextCalendar(calendar.SUNDAY)
st = cal.formatmonth(2019, 6, 0, 0)
print(st)

# create an HTML formatted calendar
print("\nHTML formatted calendar...\n")
html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
st = html_cal.formatmonth(2019, 6)
print(st)


# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
print("\nloop over the days of a month...\n")
for i in cal.itermonthdays(2019, 8):
    print(i)

  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
print("\nabbreviated days of the month according to locale...\n")
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("\nusing days to calcutae something...\n")

print("Team meetings wil be on: ")
# loop through 12 times
for m in range(1,13):
    cal = calendar.monthcalendar(2019, m)    
    week_one = cal[0]
    week_two = cal[1]

    if week_one[calendar.FRIDAY] != 0:
        meet_day = week_one[calendar.FRIDAY]
    else:
        meet_day = week_two[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meet_day))