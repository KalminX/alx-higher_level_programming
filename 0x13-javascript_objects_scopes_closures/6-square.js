#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    const char = c;
    for (let i = 0; i < this.size; i++) {
      let span = '';
      for (let i = 0; i < this.size; i++) {
        span += char;
      }
      console.log(span);
    }
  }
}

module.exports = Square;
