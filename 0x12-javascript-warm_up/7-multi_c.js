#!/usr/bin/node
const { argv } = require('node:process');

// print process.argv
let i = 0;

argv.forEach((val, index) => {
  i++;
});

if (i === 2) {
  console.log('Missing number of occurrences');
} else {
  const number = Number(argv[2]);
  for (let j = 0; j < number; j++) {
    console.log('C is fun');
  }
}
