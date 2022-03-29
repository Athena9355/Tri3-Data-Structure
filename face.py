import time
import sys
def driver():
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

if __name__ == "__main__":
    driver()