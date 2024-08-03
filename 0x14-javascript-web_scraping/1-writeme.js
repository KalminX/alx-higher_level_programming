#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

fs.writeFile(argv[2], argv[3], function (err) {
  if (err) {
    return console.log(err);
  }
});
