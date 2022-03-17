<table>
    <tr>
        <td><a href=".">Home</a></td>
        <td><a href="tt0">TT0</a></td>
        <td><a href="tt1">TT1</a></td>
    </tr>
</table>
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@AthenaWu2/TT1-Data-Structures?embed=true"></iframe>


### TT1

link to code: [here](https://replit.com/join/oyxmyaukiw-athenawu2)

```

InfoDb = [] 
InfoDb.append({  
               "FirstName": "Athena",  
               "LastName": "Wu",  
               "DOB": "May 05",  
               "Residence": "San Diego",  
               "Email": "athenaw37980@stu.powayusd.com",  
               "Fav_songs":["Closer","Life Goes On","See You Again"]  
              }) 
print("The original list:", InfoDb)
#x = InfoDb[0]["Fav_songs"][1]
#print(x)

def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
    print("\t", "Favorite songs: ", end="")
    print(", ".join(InfoDb[n]["Fav_songs"]))
    print()
  
def for_loop():
  for n in range(len(InfoDb)):
    print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return 

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)
    print("Recursive loop")
    recursive_loop(0)
print()
print()
tester()


#Fibonacci
x = input("Enter a number for fibonacci:")
def testInput(x):
  try:
    x = int(x)
    if x < 0:
      print("The input is not positive. The input needs to be positive.")
  except:
    print("The input is not an integer. The input needs to be an integer.")
  else:
      print("The input is valid. The resulting fibonacci sequence is as follows:")
      fibonacci(x)

def fibonacci(x):
  n1 = 0
  n2 = 1
  count = 0
  if x == 1:
    print(n1)
  else:
    while count < x:
      print(n1)
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1


testInput(x)

```

