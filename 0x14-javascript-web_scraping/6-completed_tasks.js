#!/usr/bin/node
const { get } = require('axios').default;
const baseUrl = process.argv[2];

get(`${baseUrl}`)
  .then(({ data }) => {
    const res = {};
    data.forEach(({ userId, completed }) => {
      if (completed) {
        res[userId] === undefined ? res[userId] = 1 : res[userId]++;
      }
    });
    console.log(res);
  })
  .catch((err) => console.error(err));
