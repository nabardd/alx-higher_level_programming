#!/usr/bin/python3
def remove_char_at(str: str, n: int) -> str:
  new = str[:]
  new = list(new)
  new.pop(n)

  new = "".join(new)

  return new

print(remove_char_at("Happy am i", 0))
