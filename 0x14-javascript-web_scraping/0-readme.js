#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

fs.readFile(argv[2], function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString());
});
