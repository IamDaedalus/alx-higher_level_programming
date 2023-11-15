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

  /* exchange the values of both width and height */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /* doubles both height and width */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
