#!/usr/bin/python3
def print_argv(argv):
  n =  len(argv) - 1

  if n == 0:
    print(f"{n:d} argument.")
    return
  elif n == 1:
    print(f"{n:d} argument: ")
  else:
    print(f"{n:d} arguments: ")

  i = 1
  
  while i <= n:
    print(f"{i:d}: {argv[i]:s}")

    i += 1

if __name__ == "__main__":
  import sys
  print_argv(sys.argv)
