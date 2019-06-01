#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  # while (x < 5):
  #     print (x)
  #     x = x + 1

  # define a for loop, are an iterator, from 5 TO 10
  # iterates through things and numbers
  print("Loop 1: ")
  for x in range(5,10):
      print (x)
      #output 5, 6, 7, 8, 9

  # use a for loop over a collection
  print("Loop 2: ")
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:    
    print (d)
 
  # use the break and continue statements
  print("Loop 3: ")
  for x in range(5, 10):
    if(x == 7): break
    print(x)
    #output 5, 6

  # using continue
  print("Loop 4: ")
  for x in range(5, 10):
    # take x divide by 2 if the value leftover == 0 then 
    # skip this and start with the next value
    if(x % 2 == 0): continue
    print(x)
    #output 5, 7, 9

  #using the enumerate() function to get index 
  # if you need a loop counter you can do it this way...
  print("Loop 5: ")
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  # enumerate(): returns the (i) index as well as the (d) value
  for i,d in enumerate(days):    
    print (i, d)



if __name__ == "__main__":
  main()
