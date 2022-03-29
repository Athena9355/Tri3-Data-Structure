import time
import sys
def driver():
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

if __name__ == "__main__":
    driver()