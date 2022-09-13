#!/usr/bin/node
const { writeFile } = require('fs').promises;
const { get } = require('axios').default;
const [,, url, path] = process.argv;

get(url)
  .then(({ data }) => writeFile(path, data, 'utf8'))
  .catch(err => console.error(err));
