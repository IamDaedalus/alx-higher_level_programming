#!/usr/bin/node

/* create new Rectangle class */
class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /* print the text representation of the Rectangle */
  print () {
    for (let i = 0; i < this.height; i++) {
      let ch = '';
      for (let j = 0; j < this.width; j++) {
        ch += 'X';
      }
      console.log(ch);
    }
  }
}
module.exports = Rectangle;
