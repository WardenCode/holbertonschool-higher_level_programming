#!/usr/bin/node
const { get } = require('axios').default;
const baseUrl = process.argv[2];

get(`${baseUrl}?completed=true`)
  .then(({ data }) => {
    const res = {};
    data.forEach(({ info: { userId } }) => {
      res[userId] !== undefined ? res[userId]++ : res[userId] = 1;
    });
    console.log(res);
  })
  .catch((err) => console.error(err));
