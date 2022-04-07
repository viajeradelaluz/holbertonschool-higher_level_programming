#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};

for (const key in dict) {
// key = '89', '90', '91', '92', '93', '94'
// dict[key] = '1', '2', '1', '3', '1', '2'
// newDict[dict[key]] = newDict['1'], newDict['2'], etc.

  if (!newDict[dict[key]]) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
