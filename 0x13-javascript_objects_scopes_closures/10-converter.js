#!/usr/bin/node

module.converter = function (base) {
  return ((num) => num.toString(base));
};
