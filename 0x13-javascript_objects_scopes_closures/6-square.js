#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w === undefined || h === undefined) {
      return this;
    }
    if (!(w <= 0 || h <= 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let i = 0; i < this.height; i++) {
      let span = "";
      for (let i = 0; i < this.width; i++) {
        span += "X";
      }
      console.log(span);
    }
  }
  double() {
    this.width += 2;
    this.height *= 2;
  }
  rotate() {
    let [x, y] = [this.width, this.height]
    this.width = y;
    this.height = x;
  }
}


class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
  charPrint(c) {
    let char = c ?? "X";
    for (let i = 0; i < this.height; i++) {
      let span = char;
      for (let i = 0; i < this.width; i++) {
        span += char;
      }
      console.log(span);
    }
  }
}

module.exports = Rectangle;
module.exports = Square;
