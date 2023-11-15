#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(Number(size), Number(size));
  }
}

module.exports = Square;
