#!/usr/bin/node
const char = 'X';
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w === 'undefined' || typeof h === 'undefined') {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }

  rotate () {
    const aux = this.width;

    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
