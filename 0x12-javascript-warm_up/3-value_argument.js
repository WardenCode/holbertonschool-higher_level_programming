#!/usr/bin/node
const { argv } = require('process');
let len = 0;

argv.forEach(() => len++);

console.log(len);
