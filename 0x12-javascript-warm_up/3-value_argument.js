#!/usr/bin/node
const args = process.argv;
const len = process.argv.length;

if (len > 2) {
  console.log(`${args[2]}`);
} else {
  console.log("No argument");
}