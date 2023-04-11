#!/usr/bin/node

exports.addMeMaybe = (num, func) => {
  num += 1;
  func();
}