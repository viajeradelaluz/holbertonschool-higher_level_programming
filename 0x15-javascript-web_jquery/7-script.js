#!/usr/bin/node

/**
 * Write a JavaScript script that fetches the character name from this
 * URL: https://swapi-api.hbtn.io/api/people/5/?format=json
 * - The name must be displayed in the HTML tag DIV#character
 * Please test with this HTML file 7-main.html
 */

const character = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then((response) => response.json())
  .then((data) => {
    const { name } = data;
    character.innerText = name;
  });
