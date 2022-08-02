#!/usr/bin/node

const { argv } = require('process');

const factorial = (num) => {
  const casted = parseInt(num);
  if (casted <= 1 || Number.isNaN(casted)) return (1);

  return (factorial(num - 1) * casted);
};

console.log(factorial(argv[2]));
