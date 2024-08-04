#!/usr/bin/node

const { argv } = require('node:process');

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }
  //   console.error("error:", error); // Print the error if one occurred
  console.log(JSON.parse(body).title); // Print the response status code if a response was received
//   console.log("body:", body); // Print the HTML for the Google homepage.
});
