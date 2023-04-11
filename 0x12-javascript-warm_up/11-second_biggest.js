#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 1) {
  console.log(1);
} else {
  let sorted = new Set(args.sort());
  sorted = [...sorted];
  console.log(sorted[sorted.length - 2]);
}

