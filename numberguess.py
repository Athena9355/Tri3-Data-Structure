import random

usern = int(input("Enter an number from 1 to 10: "))
n = random.randint(1, 10)
# print (n)

def guessNumber(usern):
    while n != "usern":
        print()
        if usern < n:
            print ("Guess Higher!")
            usern = int(input("Enter an number from 1 to 10: "))
        elif usern > n:
            print ("Guess Lower!")
            usern = int(input("Enter an number from 1 to 10: "))
        else:
            print ("Nice! That's the score you got out of 10 this week!")
            quit()


guessNumber(usern)

# def tester():
#   usern = input(int("Enter an number from 1 to 10: "))
#   guessNumber(usern)