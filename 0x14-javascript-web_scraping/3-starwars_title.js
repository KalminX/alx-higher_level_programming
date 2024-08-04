#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

request(argv[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }
  console.log(JSON.parse(body)); // Print the response status code if a response was received
});
