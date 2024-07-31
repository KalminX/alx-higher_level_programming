#!/usr/bin/node
const { argv } = require('node:process');

// print process.argv
if (argv.length === 2) {
  console.log('No argument');
} else {
  for (let i = 2; i < argv.length; i++) {
    console.log(argv[i]);
  }
}
