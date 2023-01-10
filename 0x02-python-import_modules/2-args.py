#!/usr/bin/python3
def print_argv(argv):
    n =  len(argv) - 1

    if n == 0:
      print("{:d} arguments.".format(n))
      return
    elif n == 1:
      print("{:d} argument: ".format(n))
    else:
      print("{:d} arguments: ".format(n))

    i = 1
    
    while i <= n:
      print("{:d}: {:s}".format(i, argv[i]))

      i += 1


if __name__ == "__main__":
    import sys
    print_argv(sys.argv)
