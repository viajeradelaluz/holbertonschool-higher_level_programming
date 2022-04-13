#!/usr/bin/node

/**
 * Write a script that gets the contents of a webpage and stores it in a file.
 * - The first argument is the URL to request
 * - The second argument the file path to store the body response
 * - The file must be UTF-8 encoded
 * - You must use the module request
 */

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const destination = process.argv[3];

request(url, function (err, response, body) {
  if (err) console.log(err);
  else {
    fs.writeFile(destination, body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
