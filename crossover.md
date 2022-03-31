{% include navigation.html %}

# Crossover Coding

## Code Snippets

### Code for math guess game function
```python
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
```
### Code for random password generator
```python
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

```


