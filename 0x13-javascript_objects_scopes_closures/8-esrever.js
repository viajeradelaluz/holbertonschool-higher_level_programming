#!/usr/bin/node
exports.esrever = function (list) {
  const listReverse = [];
  for (const i in list) {
    listReverse.unshift(list[i]);
  }
  return listReverse;
};
