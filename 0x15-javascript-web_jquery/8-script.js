#!/usr/bin/node

/**
 * Write a JavaScript script that fetches and lists the title for all movies
 * by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
 * - All movie titles must be list in the HTML tag UL#list_movies
 * Please test with this HTML file 8-main.html
 */

const moviesList = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then((response) => response.json())
  .then((data) => {
    for (movies of data.results) {
      const movieItem = document.createElement('li');
      movieItem.textContent = movies.title;
      moviesList.appendChild(movieItem);
    }
  });
