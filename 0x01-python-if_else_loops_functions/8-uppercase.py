#!/usr/bin/python3
def uppercase(str):
  for char in str:
    if ord(char) in range(97, 123):
      print(f"{chr(ord(char) - 32)}", end='')
