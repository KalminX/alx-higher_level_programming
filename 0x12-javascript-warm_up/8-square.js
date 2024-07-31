#!/usr/bin/node
const { argv } = require('node:process');

// print process.argv
let i = 0;

argv.forEach((val, index) => {
  i++;
});

if (i === 2) {
  console.log('Missing size');
} else if (Boolean(Number(argv[2])) === true) {
  const number = Number(argv[2]);
  for (let j = 0; j < number; j++) {
    let width = '';
    for (let j = 0; j < number; j++) {
      width += 'X';
    }
    console.log(width);
  }
} else {
  console.log('Missing size');
}
