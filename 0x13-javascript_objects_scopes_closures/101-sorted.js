#!/usr/bin/node
const { dict } = require('./101-data');

const result = {};

for (const [key, value] of Object.entries(dict)) {
  if (!(result[value])) {
    result[value] = [];
  }
  result[value].push(key);
}
console.log(result);
