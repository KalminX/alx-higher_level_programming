#!/usr/bin/node
const { argv } = require('node:process');

function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}

// console.log(factorial(4));

if (argv.length === 2) {
  console.log(1);
} else {
  console.log(factorial(Number(argv[2])));
}
