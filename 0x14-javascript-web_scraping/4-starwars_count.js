#!/usr/bin/node
const { get } = require('axios').default;
const urlSearch = 'https://swapi-api.hbtn.io/api/people/18/';

get(process.argv[2])
  .then(({data: { results }}) => {
    let count = 0;
    for (const film of results) {
      if (film.characters.some(url => url === urlSearch)) { count++; }
    }
    console.log(count);
  })
  .catch(err => console.error(err));
