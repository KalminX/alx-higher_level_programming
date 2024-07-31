#!/usr/bin/node
const { argv } = require('node:process');

// print process.argv
if (Boolean(Number(argv[2])) === true) {
  console.log(`My number: ${argv[2]}`);
} else {
  console.log('Not a number');
}
