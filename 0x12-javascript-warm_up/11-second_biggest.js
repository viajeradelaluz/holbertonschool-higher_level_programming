#!/usr/bin/node
const args = process.argv.slice(2);
let number = 0;

function compareNumbers (a, b) {
  return a - b;
}

if (args.length > 1) {
  args.sort(compareNumbers);
  number = args[args.length - 2];
}
console.log(number);
