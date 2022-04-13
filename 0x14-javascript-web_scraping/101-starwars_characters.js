#!/usr/bin/node

/**
 * Write a script that prints all characters of a Star Wars movie:
 * - The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * - Display one character name by line
 * - You must use the Star wars API
 * - You must use the module request
 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

const syncChars = ([firstUrl, ...characters]) => {
  if (!firstUrl) {
    return;
  }
  request(firstUrl, function (err, _, body) {
    if (err) console.log(err);
    else {
      const { name } = JSON.parse(body);
      console.log(name);
    }
    syncChars(characters);
  });
};

request(`${url}${movieId}`, function (err, _, body) {
  if (err) console.log(err);
  else {
    const { characters } = JSON.parse(body);
    syncChars(characters);
  }
});
