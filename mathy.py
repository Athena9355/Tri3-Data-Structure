import random
import string


# Fibonacci
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
                return (recur_fibo(x - 1) + recur_fibo(x - 2))

        for i in range(x):
            print(recur_fibo(i))


def factorial():
    def recur_factorial(n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * recur_factorial(n - 1)

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
                for i in range(num, 1, -1):
                    result = result * i
                # result = num
                # while num >= 1:
                # print (num)
                # print (result)
                # result = result * (num - 1)
                # num = num - 1
            print("The factorial of", initial, "is", result)

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
        for i in range(1, small + 1):
            if ((x % i == 0) and (y % i == 0)):
                gcf = i

        return gcf

    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    result = computeGCF(a, b)
    # prints 12
    print("The GCF of", a, "and", b, "is: ", result)


def gcf_oop():
    print("gcf oop")
    a = input("enter the first number: ")
    b = input("enter the second number: ")

    def computeGCF(x, y):
        if x > y:
            small = y
        else:
            small = x
        for i in range(1, small + 1):
            if ((x % i == 0) and (y % i == 0)):
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
                print("the greatest common factor of", a, "and", b, "is", computeGCF(a, b))

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
            print("Guess Lower!")
            usern = int(input("Enter an number from 1 to 10: "))
        elif usern < n:
            print("Guess Higher!")
            usern = int(input("Enter an number from 1 to 10: "))
        elif usern == n:
            print("Nice! That's the score you got out of 10 this week!")
            break


def tester():
    usern = int(input("Enter an number from 1 to 10: "))
    guessNumber(usern)


def password(l):
    letter = string.ascii_lowercase + string.ascii_uppercase
    n = string.digits
    other = string.punctuation
    all = letter + n + other
    for i in range(l):
        password = random.sample(all, l)
    for thing in password:
        print(thing, end='')
    print(" ")


def passwordtester():
    l = int(input("Enter a desired length for the password: "))
    password(l)


def game():
    # builds the list of words available to be answers
    words = [
        "hello",
        "games",
        "about",
        "agent",
        "human",
        "pause",
        "board",
        "audio",
        "crate",
    ]
    # randomly pick a word from the list and save it as the correct answer
    answer = random.choice(words)
    # creates a blank list that is used to save every letter of the chosen word
    letter = []
    # adds letter to the list letter
    for i in answer:
        letter.append(i)
    # makes sure that every code worked as intended
    print(answer)
    print(letter)

    print("Hello, welcome to the game!\n"
          "The computer will generate a random word.\n"
          "You have to guess, one letter at a time, what the word is.\n"
          "You have a limited number of chances to guess the wrong letter.\n")
    n = int(input("How many chances would you like to have?"))

    print("let's start the game! Each blank below represents a letter.")
    blank = "__ "
    num_blank = blank * len(letter)
    blank_list = [num_blank]
    print(blank_list)
    progress = letter
    save = ["__ ", "__ ", "__ ", "__ ", "__ "]
    while n > 0:
        guess = input("Guess a letter!: ")
        for i in range(
                len(letter)):  # picks the correct letter from the list letter. i.e. output num = a letter, not an index
            if letter[i] == guess:  # if the num is a correct guess
                progress[i] = guess
                # print("letter is in the word at position", i + 1)
                print(progress[i])
                save[i] = guess
                print(save)
                n = n + 1
        n = n - 1
        if save == letter:
            print("Congratulations! You have solved the word! The word is ", answer)
            break
    print("Sorry, you went out of guesses! Try again! The answer is", answer)