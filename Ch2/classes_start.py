#
# Example file for working with classes
#


# creating the class!, if we were inheriting it would be like this guy
# class myClass(theInhertingClass)
class myClass():
  # 'self', is like the 'this' keyword
  def classMethod(self):
    print("myClass' classMethod!")

  def classMethod2(self, someString):
    print("myClass' classMethod2! " + someString)

# inheriting myClass()
class anotherClass(myClass):
  # 'self', is like the 'this' keyword
  def classMethod(self):
    myClass.classMethod(self)
    print("anotherClass' classMethod!")

  def classMethod2(self, someString):
    print("anotherClass' classMethod2! " + ": I am doing my own thing")


def main():
  # don't have to call self, it is handled by the interprator
  c = myClass()
  c.classMethod()
  c.classMethod2("wowweeee")

  # instatiating the class
  c2 = anotherClass()
  c2.classMethod()
  c2.classMethod2("Did a won?")
  
if __name__ == "__main__":
  main()
