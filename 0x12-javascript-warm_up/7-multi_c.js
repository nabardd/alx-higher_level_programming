#!/usr/bin/node
const args = process.argv[2];

if (Number(args)) {
  for (let i = 0; i < args; i++) {
    console.log("C is fun");
  }
} else {
  console.log('Missing number of occurences');
}