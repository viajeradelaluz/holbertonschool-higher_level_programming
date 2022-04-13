#!/usr/bin/node

/**
 * Write a script that prints the number of movies where the character “Wedge Antilles” is present.
 * - The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
 * - Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
 * - You must use the module request
 */

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) console.log(err);
  else {
    const films = JSON.parse(body).results;
    let count = 0;

    for (const filmID of films) {
      for (const character of filmID.characters) {
        // Wedge Antilles is character ID 18
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
