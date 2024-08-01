#!/usr/bin/node
const { argv } = require('node:process');

const numbers = argv.slice(2).map(x => Number(x));
const biggestNumber = numbers.sort().reverse()[0];

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  console.log(biggestNumber);
}
