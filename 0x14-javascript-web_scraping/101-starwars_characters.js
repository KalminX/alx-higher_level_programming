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
  const characterNames = [];
  let completedRequests = 0;
  characters.forEach((url, index) => {
    request(url, function (error, response, body) {
      if (error) {
        console.log('error:', error);
      }
      try {
        const name = JSON.parse(body).name;
        characterNames[index] = name;
      } catch (e) {
        console.error('Invalid JSON:', e);
        return;
      }
      completedRequests++;
      if (completedRequests === characters.length) {
        characterNames.forEach((name) => console.log(name));
      }
    });
  });
});
