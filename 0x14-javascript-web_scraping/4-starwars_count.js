#!/usr/bin/node
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(({ data: { results } }) => {
    let count = 0;
    results.forEach(({ characters }) => {
      characters.forEach((url) => {
        if (url.includes('18')) count++;
      });
    });
    console.log(count);
  })
  .catch(err => console.error(err));
