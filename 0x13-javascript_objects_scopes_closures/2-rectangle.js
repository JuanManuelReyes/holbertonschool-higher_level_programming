#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w === 'undefined' || typeof h === 'undefined') {
      return;
    }
    this.width = w;
    this.height = h;
  }
};
