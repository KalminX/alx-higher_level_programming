#!/usr/bin/node
const arr = require('./100-data').list;

const newArr = [...arr].map(x => x * arr.indexOf(x));

console.log(arr);
console.log(newArr);
