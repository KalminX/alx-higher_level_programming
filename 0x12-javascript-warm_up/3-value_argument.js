#!/usr/bin/node
const { argv } = require('node:process');

// print process.argv
let i = 0;

argv.forEach((val, index) => {
  i++;
});

if (i === 2) {
  console.log('No argument');
} else if (i === 3) {
  console.log(argv[i - 1]);
}
