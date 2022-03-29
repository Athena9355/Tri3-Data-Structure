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

if __name__ == "__main__":
    driver()