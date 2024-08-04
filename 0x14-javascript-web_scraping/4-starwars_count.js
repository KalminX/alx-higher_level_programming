#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }
  const movies = JSON.parse(body).results;
  const characters = movies.map((movie) => movie.characters);

  let count = 0;
  characters.forEach((character) => {
    character.forEach((occurrence) => {
      if (occurrence.includes('18')) {
        count += 1;
      }
    });
  });
  console.log(count);
});
