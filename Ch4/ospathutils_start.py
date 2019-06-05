#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print("PC OS:", os.name)

  # Check for item existence and type
  test_file = "textfile.txt"
  spacer = "\n"

  print(spacer)
  print("Item Exists: " + str(path.exists(test_file)))
  print("Item is a file: " + str(path.isfile(test_file)))
  print("Item is a Directory: " + str(path.isdir(test_file)))

  # Work with file paths
  print(spacer + "getting the items full path...")
  print("Items path is: " + str(path.realpath(test_file)))
  print("Item path and name: " + str(path.split(path.realpath(test_file))))

  
  # Get the modification time
  print(spacer + "Getting the Files Modified time...")
  
  #2 ways to do the same thing...
  #1st way
  t = time.ctime(path.getmtime(test_file))
  print("last modified: " + t)
  #2nd way
  print(datetime.datetime.fromtimestamp(path.getmtime(test_file)))
  
  # Calculate how long ago the item was modified
  # figuring out how long ago it was last touched !
  print(spacer + "How long ago it was last changed: ")

  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(test_file))

  print(str(td))
  print("Or: " + str(td.total_seconds()) + " seconds")
  
if __name__ == "__main__":
  main()
