#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil


def main():

  test_file = "textfile.txt"

  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    print("\n")
    source = path.realpath(test_file)

    
    # let's make a backup copy by appending "bak" to the name
    dst = source + ".bak"
    
    # copy over the permissions, modification times, and other info
    shutil.copy(source, dst) # this copies contents
    # if you want the file metadata
    shutil.copystat(source, dst)

    # rename the original file

    
    # now put things into a ZIP archive


    # more fine-grained control over ZIP files

      
if __name__ == "__main__":
  main()
