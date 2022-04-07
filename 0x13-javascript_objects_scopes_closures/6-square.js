#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let row = 0; row < this.width; row++) {
        console.log(c.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
