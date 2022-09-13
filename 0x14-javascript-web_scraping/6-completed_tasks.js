#!/usr/bin/node
const { get } = require('axios').default;
const baseUrl = process.argv[2];

get(`${baseUrl}`)
  .then(({ data }) => {
    const res = {};
    data.forEach(({ userId, completed }) => {
      if (res[userId] === undefined) res[userId] = 0;
      if (completed) res[userId] += 1;
    });
    console.log(res);
  })
  .catch((err) => console.error(err));
