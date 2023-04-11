#!/usr/bin/node
const args = process.argv.length;

if (args === 0) {
  console.log("No argument");
} else if (args === 1) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
}