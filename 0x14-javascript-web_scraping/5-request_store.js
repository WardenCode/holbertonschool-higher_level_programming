#!/usr/bin/node
const { writeFile } = require('fs');
const { get } = require('axios').default;
const [,, url, path] = process.argv;

get(url)
  .then(({ data }) => writeFile(path, data, 'utf8', (err) => {
    if (err) console.error(err);
  }))
  .catch(err => console.error(err));
