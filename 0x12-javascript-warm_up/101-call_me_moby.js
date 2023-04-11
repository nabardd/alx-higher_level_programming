#!/usr/bin/node

exports.callMeMoby = (num, func) => {
  while (num) {
    func();
    num -= 1;
  }
}
