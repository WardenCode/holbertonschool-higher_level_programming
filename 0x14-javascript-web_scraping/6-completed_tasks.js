#!/usr/bin/node
const { get } = require('axios').default;
const baseUrl = process.argv[2];

get(`${baseUrl}?completed=true`)
  .then(({ data }) => {
    const res = {};
    for (const info of data) {
      const userId = info.userId;
      res[userId] ? res[userId]++ : res[userId] = 1;
    }
    console.log(res);
  })
  .catch((err) => console.error(err));
