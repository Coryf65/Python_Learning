#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
#need the make archive module
from shutil import make_archive


def main():

  test_file = "textfile.txt"
  new_test = "newfile.txt"

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
    os.rename(test_file, new_test)
    
    # now put things into a ZIP archive

    # need to get the file path 
    root_dir, tail = path.split(source)

    shutil.make_archive("ArchiveFiles", "zip", root_dir)

    # more fine-grained control over ZIP files

      
if __name__ == "__main__":
  main()
