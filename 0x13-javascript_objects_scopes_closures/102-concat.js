#!/usr/bin/node

const { argv } = require('node:process');

const fs = require('fs');

const file1 = fs.readFileSync(`./${argv[2]}`);
const file2 = fs.readFileSync(`./${argv[3]}`);
const text = `${file1.toString()}\n${file2.toString()}\n`;
fs.writeFileSync(argv[4], text);
