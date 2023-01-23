#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    try:
        while True:
          if index < x:
              if isinstance(my_list[index], int):
                  print("{:d}".format(my_list[index]), end="")
              index += 1
          else:
            print()
            return (index)
    except IndexError:
        print()
        return (index)
