#!/usr/bin/node

/**
 * Write a script that computes the number of tasks completed by user id.
 * - The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * - Only print users with completed task
 * - You must use the module request
 */

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) console.log(err);
  else {
    const json = JSON.parse(body);
    const usersTaksOK = {};

    for (const item of json) {
      if (!item.completed) {
        continue;
      }
      const { userId, completed } = item;
      if (usersTaksOK[userId] === undefined) {
        usersTaksOK[userId] = 0;
      }
      usersTaksOK[userId] += Number(completed);
    }
    console.log(usersTaksOK);
  }
});
