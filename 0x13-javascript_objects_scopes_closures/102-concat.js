#!/usr/bin/node

// Files to concatenate
const fileA = process.argv[2];
const fileB = process.argv[3];

// Destination file
const fileC = process.argv[4];

// Reading the files
const fs = require('fs');
const dataA = fs.readFileSync(fileA, 'utf-8');
const dataB = fs.readFileSync(fileB, 'utf-8');

// Saving the data in destination file
fs.writeFileSync(fileC, dataA + dataB);
