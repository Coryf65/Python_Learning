#
# Example file for working with date information
#

# like a using in C#
from datetime import date
from datetime import time
from datetime import datetime

def main():

  print("using the date class...\n")

  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  # formatting the date too ! heehee
  today = date.today()

  print(f"Today's date is: {today:%m-%d-%Y}")

  # print out the date's individual components
  print("Date Components: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday), adding one to make more sense to me
  print("todays weekday number is: ", today.weekday()+1)
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  print("Which is a: ", days[today.weekday()])


  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  print("\nusing the datetime class...\n")

  today1 = datetime.now()
  print(f"Current date is: {today1}")

  # Get the current time
  time = datetime.time(today1)
  print("getting the current time...")
  print(time)

  
if __name__ == "__main__":
  main()
  