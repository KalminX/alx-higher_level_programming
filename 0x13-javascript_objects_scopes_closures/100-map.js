#!/usr/bin/node
const list = require('./100-data').list;

const newArr = [...list].map(x => x * list.indexOf(x));

console.log(list);
console.log(newArr);
