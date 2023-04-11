#!/usr/bin/node
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

const add = (arg_a, arg_b) => {
  if (arg_a && arg_b) {
    console.log(`${ arg_a + arg_b}`);
  } else {
    console.log('NaN');
  }
}

add(a, b);