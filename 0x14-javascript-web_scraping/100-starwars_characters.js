#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }
  let characters;
  try {
    characters = JSON.parse(body).characters;
  } catch (e) {
    console.log('Invalid JSON:', e);
    return;
  }
  characters.forEach(url => {
    request(url, function (error, response, body) {
      if (error) {
        console.log('error:', error);
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  });
});
