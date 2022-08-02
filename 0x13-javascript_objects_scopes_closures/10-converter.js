#!/usr/bin/node
exports.converter = function (base) {
  function parser (num) {
    return num.toString(base);
  }
  return parser;
};
