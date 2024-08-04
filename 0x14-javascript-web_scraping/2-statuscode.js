#!/usr/bin/node

const { argv } = require('node:process');

const request = require('request');
request(argv[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }
  //   console.error("error:", error); // Print the error if one occurred
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
//   console.log("body:", body); // Print the HTML for the Google homepage.
});
