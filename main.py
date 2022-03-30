import tree
import swap
import numpad
import face
import arrow
import mathy
import info


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
    ["Fibonacci", mathy.fib],
    ["Factorial", mathy.factorial],
    ["Factorial with class", mathy.test],
    ["Palindrome", mathy.palindrome],
    ["Greatest common factor (imperative form)", mathy.gcf_imperative],
    ["Greatest common factor (OOP form)", mathy.gcf_oop],
    ["Guess Number Game!", mathy.tester],
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


# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    menu(title, sub_menu)

def driver():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu(title, menu_list)


if __name__ == "__main__":
    driver()

