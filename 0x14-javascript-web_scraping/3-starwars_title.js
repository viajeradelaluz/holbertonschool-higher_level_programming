#!/usr/bin/node

/**
 * Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
 * - The first argument is the movie ID
 * - You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
 * - You must use the module request
 */

const request = require('request');
const starWarsAPI = 'https://swapi-api.hbtn.io/api/films/';
const episode = process.argv[2];

request(`${starWarsAPI}${episode}`, function (err, response, body) {
  if (err) console.log(err);
  else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
