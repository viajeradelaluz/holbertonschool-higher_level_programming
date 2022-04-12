#!/usr/bin/node

/**
 * Write a script that writes a string to a file.
 * - The first argument is the file path
 * - The second argument is the string to write
 * - The content of the file must be written in utf-8
 * - If an error occurred during while writing, print the error object
 */

const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];

fs.writeFile(file, data, 'utf-8', (err) => {
  if (err) console.log(err);
});
