#!/usr/bin/python3
def sum_args(argv):
  n = len(argv) - 1
  if n == 0:
    print(f"{n:d}")
  else:
    sum = 0
    for i in range(1, len(argv) + 1):
      sum += int(argv[i])

    print(f"{sum:d}")

if __name__ == "__main__":
  import sys
  sum_args(sys.argv)
