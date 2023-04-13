#!/usr/bin/node

let count = 0;

module.exports.logme = (item) => {
  console.log(`${count}: ${item}`);
}