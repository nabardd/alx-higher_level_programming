#!/usr/bin/node
const arg = Number(process.argv[2]);

if (arg) {
  for (let i = 0; i < arg; i++) {
    let line = '';
    for (let j = 0; j < arg; j++) {
      line += 'X';
    }
    console.log(line);
  }

} else {
  console.log('Missing size');
}