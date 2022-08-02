#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

let content = '';

content += fs.readFileSync(argv[2], 'utf8');

content += fs.readFileSync(argv[3], 'utf8');

fs.writeFileSync(argv[4], content, 'utf8');
