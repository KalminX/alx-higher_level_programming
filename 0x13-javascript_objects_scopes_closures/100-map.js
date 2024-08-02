#!/usr/bin/node
const list = require('./100-data').list;

const newArr = [...list].map((num, index) => num * index);

console.log(list);
console.log(newArr);
