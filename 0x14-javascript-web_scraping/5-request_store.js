#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');
const fs = require('fs');

request(argv[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }
  fs.writeFile(argv[3], body, function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
