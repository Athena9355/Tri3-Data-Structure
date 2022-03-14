<table>
    <tr>
        <td><a href=".">Home</a></td>
    </tr>
</table>

<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/join/iwszcdjzqd-athenawu2">
</iframe>


### TT0
Build your own menu and sub-menu
Add swap and keypad from Tri 2 Week 10, to your project and menu.
For additional challenge and review, build a Christmas tree with *s or a pattern of your choice
Add two items below to get ready for animations and interacting with terminal codes

link to code: [here](https://replit.com/join/agfpfyziww-athenawu2)

```

import time
import sys
#swap function from tri 2#
def swap_input():
  list = []
  age1 = input("Enter the first number:")
  age2 = input("Enter the second number:")
  def swap(num1, num2):
    if age1 > age2:
      list.append(age2)
      list.append(age1)
    if age1 < age2:
      list.append(age1)
      list.append(age2)
  swap(age1,age2)
  print("the swapped result (from least to greatest)", list)
#swap function ends#

#number pad
def numPad():
  print()
  numbers = ['1 2 3','4 5 6','7 8 9','  0  ']
  number_pad = '\n'.join(numbers)
  print(number_pad)
#number pad end

#christmas
def christmas():
  top = '⭐️'
  top_center = top.center(20, " ")
  print(top_center,end='')
  for i in range(10):
    star = '*' * (2*i)
    center_star = star.center(20, " ")
    print(center_star)
  print('       ||||||')
  print('       ||||||')
#christmas ends

#animation
def animation():
  bright_star = "😯"
  dim_star = "😉"
  for i in range(3):
      print(bright_star)
      time.sleep(0.5)
      sys.stdout.write("\033[F") #goes back to previous line
      sys.stdout.write("\033[K") #clears the line
      print(dim_star)
      sys.stdout.write("\033[F")
      sys.stdout.write("\033[K")
      time.sleep(0.5)

def move():
  for i in range(3):
    print("=>")
    time.sleep(0.5)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print("  =>")
    time.sleep(0.5)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print("    =>")
    time.sleep(0.5)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print("      =>")
    time.sleep(0.5)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print("        =>")
    time.sleep(0.5)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    
#animation ends

#menu challenge
def print_menu():
  menu_list = [
    '1-- number pad',
    '2-- number swap',
    '3-- christmas tree',
    '4-- print submenu for animation'
  ]
  menu = '\n'.join(menu_list)
  print(menu)

def print_submenu():
  menu_list = [
    '5-- animation 1',
    '6-- animation 2'
  ]
  menu = '\n'.join(menu_list)
  print(menu)

  
def print_result():
  if choice == "1":
    print()
    print('\n'"chocie 1" '\n')
    numPad()
    print()
    
  if choice == "2":
    print()
    print('\n'"chocie 2" '\n')
    swap_input()
    print()
    
  if choice == "3":
    print()
    print('\n'"chocie 3" '\n')
    christmas()
    print()

  if choice == "4":
    print()
    print_submenu()
    print("Choose an animation:")
    choiceanimation = input("Enter your choice:")
    if choiceanimation == "5":
      print()
      print('\n'"choice 5" '\n')
      move()
      print()
    
    if choiceanimation == "6":
      print()
      print('\n'"chocie 6" '\n')
      animation()
      print()
    print()



while(True):
  print("Menu Challenge:")
  print_menu()
  choice = input("Enter your choice:")
  print_result()

```
