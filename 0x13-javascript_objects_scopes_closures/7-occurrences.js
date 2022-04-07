#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      occurrences += 1;
    }
  }
  return occurrences;
};
