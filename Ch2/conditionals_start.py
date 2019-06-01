#
# Example file for working with conditional statements
#

def main():
  # declaring many vars inline
  x, y = 100, 100
  
  # conditional flow uses if, elif (else if, in C#), else  
  # can use string interpolation using the keyword f"{var/object}"
  if (x < y):
    st = f"{x} is less than {y}"
  elif(x == y):
    st = f"{x} is the same as {y}"
  else:
    st = f"{x} is greater than {y}"
  print(st)

  # like a case statement, or switch statements, NOPE!!! just else if's
  
  # conditional statements let you use "a if C else b", just a shorthand if else similar to the turinary statement
  st = "x is less than y" if (x<y) else "x is greater than y"
  print(st)   


if __name__ == "__main__":
  main()
