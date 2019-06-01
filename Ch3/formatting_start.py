#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()

  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A shortname/Fullname - weekday, %b/%B - month shortname/Fullname, %d - day of month

  # using the, str f time method
  print("\n" + "Parsing the date object...\n")  
  print(now.strftime("The current year is: %y"))
  print(now.strftime("The current Weekday is: %B"))
  print(now.strftime("The current day of the month is: %d"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print("\n" + "showing time to what region the pc acessing is in...\n")  
  print(now.strftime("locale's date and time: %c"))
  print(now.strftime("locale's date %x"))
  print(now.strftime("locale's time: %X"))


  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print("\n" + "Formatting the time...\n")  
  print(now.strftime("Current time: %I:%M:%S %p"))  
  print(now.strftime("24-hour time: %H:%M"))  



if __name__ == "__main__":
  main(); #linter says this semi colon is uneeded
