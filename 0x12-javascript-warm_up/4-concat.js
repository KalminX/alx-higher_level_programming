#!/usr/bin/node
const { argv } = require('node:process');

// print process.argv
let i = 0;

argv.forEach((val, index) => {
  i++;
});

if (i === 2) {
  console.log('undefined is undefined');
} else if (i === 3) {
  console.log(`${argv[2]} is undefined`);
} else if (i === 4) {
  console.log(`${argv[2]} is ${argv[3]}`);
}
