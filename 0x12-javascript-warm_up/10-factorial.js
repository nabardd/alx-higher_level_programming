#!/usr/bin/node
const arg = Number(process.argv[2]);

const factorial = (number) => {
  if (number === 0 || isNaN(number)) {
    return 1
  } else {
    return number * factorial(number - 1);
  }
}

console.log(factorial(arg));