#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(Number(size), Number(size));
  }

  /* print a square using X by default */
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let ch = '';
      for (let j = 0; j < this.width; j++) {
        ch += c;
      }
      console.log(ch);
    }
  }
}

module.exports = Square;
