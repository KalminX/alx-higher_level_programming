#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) {
      return this;
    }
    if (!(w <= 0 || h <= 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let span = '';
      for (let i = 0; i < this.width; i++) {
        span += 'X';
      }
      console.log(span);
    }
  }

  double () {
    this.width += 2;
    this.height *= 2;
  }

  rotate () {
    const [x, y] = [this.width, this.height];
    this.width = y;
    this.height = x;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
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

module.exports = Rectangle;
module.exports = Square;
