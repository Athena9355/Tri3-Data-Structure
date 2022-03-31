import random
import string
#Fibonacci
def fib():
    x = input("Enter a number for fibonacci:")
    try:
      x = int(x)
      if x < 0:
        print("The input is not positive. The input needs to be positive.")
    except:
      print("The input is not an integer. The input needs to be an integer.")
    else:
        def recur_fibo(x):
           if x <= 1:
             return x
           else:
             return(recur_fibo(x-1) + recur_fibo(x-2))
        for i in range(x):
            print(recur_fibo(i))




def factorial():   
    def recur_factorial(n):
      if n == 1 or n == 0:
          return 1
      else:
          return n * recur_factorial(n-1)
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))


def test():
  num = int(input("Enter a number: "))
  initial = num
  if num < 0:
    print("the input has to be positive")
    return
  class factorial:
    def __init__(self):
        pass
    # Defining __call__ method
    def __call__(self, num):
      if num == "1" or num == "0":
        result = 1
      elif num < 0:
        print()
        print("the input has to be positive")
      else: 
        result = 1
        for i in range (num, 1, -1):
          result = result * i
        #result = num
        #while num >= 1:
          #print (num)
          #print (result)
          #result = result * (num - 1)
          #num = num - 1
      print("The factorial of", initial ,"is", result)
  # Instance created
  ans = factorial()
  # __call__ method will be called
  ans(num)


def gcf_imperative():
  def computeGCF(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcf = i
              
    return gcf
  
  a = int(input("enter the first number: "))
  b = int(input("enter the second number: "))
  result = computeGCF(a, b)
  # prints 12
  print ("The GCF of", a, "and", b, "is: ",result) 


def gcf_oop():
  print("gcf oop")
  a = input("enter the first number: ")
  b = input("enter the second number: ")
  def computeGCF(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcf = i
              
    return gcf
  
  class Product:
    def __init__(self):
        pass

    def __call__(self, a, b):
      try:
        a = int(a)
      except:
        print("The input is not an integer. The input needs to be an integer.")
      try:
        b = int(b)
      except:
        print("The input is not an integer. The input needs to be an integer.")
      if a < 0 or b < 0:
        print("the number needs to be positive")
        return
      else:
        print("the greatest common factor of", a, "and", b, "is", computeGCF(a,b))
  
  # Instance created
  ans = Product()
    
  # __call__ method will be called
  ans(a, b)

def palindrome():
  print("palindrome")




def guessNumber(usern):
    n = random.randint(1, 10)
    while n != "usern":
        if usern > n:
            print ("Guess Lower!")
            usern = int(input("Enter an number from 1 to 10: "))
        elif usern < n:
            print ("Guess Higher!")
            usern = int(input("Enter an number from 1 to 10: "))
        elif usern == n:
            print ("Nice! That's the score you got out of 10 this week!")
            quit()

def tester():
    usern = int(input("Enter an number from 1 to 10: "))
    guessNumber(usern)

def password():
    letter = string.ascii_lowercase + string.ascii_uppercase
    n = string.digits
    other = string.punctuation
    all = letter + n + other
    password = random.sample(all, 8)
    print (password)