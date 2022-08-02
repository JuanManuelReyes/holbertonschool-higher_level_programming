#!/usr/bin/node
const SquareConstructor = require('./5-square');
const charC = 'C';

module.exports = class Square extends SquareConstructor {
  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(charC.repeat(this.width));
      }
    }
  }
};
