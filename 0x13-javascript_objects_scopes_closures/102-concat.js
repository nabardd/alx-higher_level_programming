#!/usr/bin/node

const args = process.argv.slice(2);

const fs = require('fs');

const fileA = fs.readFileSync(args[2], 'utf-8');
const fileB = fs.readFileSync(args[3], 'utf-8');

fs.writeFileSync(args[4], fileA + fileB);