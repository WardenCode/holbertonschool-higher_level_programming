#!/usr/bin/node

module.converter = function (base) {
  return function (num) {
    num.toString(base);
  }
}
