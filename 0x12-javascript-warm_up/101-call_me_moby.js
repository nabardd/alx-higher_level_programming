#!/usr/bin/node

const callMeMoby = (num, func) => {
  while (num) {
    func();
    num -= 1;
  }
}