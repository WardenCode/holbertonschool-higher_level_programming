#!/usr/bin/node
const { get } = require('axios').default;

get(process.argv[2])
  .then(({ status }) => console.log(`code: ${status}`))
  .catch(({ response: { status } }) => console.log(`code: ${status}`));
