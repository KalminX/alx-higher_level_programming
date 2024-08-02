#!/usr/bin/node
const arr = require('./100-data').list;

const new_arr = [...arr].map(x => x * arr.indexOf(x));

console.log(arr);
console.log(new_arr);
