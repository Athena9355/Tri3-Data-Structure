# Tri3 Data Structure
<table>
    <tr>
        <td><a href=".">Home</a></td>
        <td><a href="tpt">TPT Notes</a></td>
        <td><a href="tt">TT Notes and Codes</a></td>
        <td><a href="cb">CB requirements etc.</a></td>
    </tr>
</table>
<table>
    <tr>
        <td><a href="https://github.com/Athena9355/Tri3-Data-Structure/issues/1">Week 0 review ticket</a></td>
        <td><a href="https://github.com/Athena9355/Tri3-Data-Structure/issues/2">Week 1 review ticket</a></td>
    </tr>
</table>
  
<hr>


### Timebox
- **Week 0**:
    - Menu set up
    ```
    border = "=" * 25
    banner = f"\n{border}\nPlease Select An Option\n{border}"

    main_menu = [
        ["Number Pad", numpad.driver],
        ["Number Swap", swap.driver],
        ["Christmas Tree", tree.driver],
        ["Animation (arrow)", arrow.driver],
        ["Animation (face)", face.driver],
        ["List (Loops)", info.driver],
    ]


    sub_menu = [
        ["Fibonacci", math.fib],
        ["Factorial", math.factorial],
    ]


    def menu(banner, options):
        # header for menu
        print(banner)
        # build a dictionary from options
        prompts = {0: ["Exit", None]}
        for op in options:
            index = len(prompts)
            prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    menu(banner, options)  # recursion, start menu over again
    
    ```
    - Christmas Tree
    ```
    def driver():
      top = '⭐️'
      top_center = top.center(20, " ")
      print(top_center,end='')
      for i in range(10):
        star = '*' * (2*i)
        center_star = star.center(20, " ")
        print(center_star)
      print('       ||||||')
      print('       ||||||')

    ```

    - Matrix (number pad)
    ```
    def driver():
      print()
      numbers = ['1 2 3','4 5 6','7 8 9','  0  ']
      number_pad = '\n'.join(numbers)
      print(number_pad)
    
    ```
    - Swap
    ```
    def driver():
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
    ```
- **Week 1**:
    - Car List
    ```
    def driver():   
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
    ```
    - Fibonacci
    ```
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
    
    ```
    - Factorial:
    ```
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
    ```
- Week 2: 
    - Factorial Class
    - Math imperative and Class
    - Palindrome imperative and class
