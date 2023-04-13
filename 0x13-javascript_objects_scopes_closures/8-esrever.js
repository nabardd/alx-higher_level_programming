#!/usr/bin/node

module.exports.esrever = (list) => {
  let tmp;
  let last = list.length - 1;

  for (let i = 0; i < list.length / 2; i++) {
    tmp = list[i];
    list[i] = list[last - i];
    list[last - i] = tmp;
  }

  return (list);
}