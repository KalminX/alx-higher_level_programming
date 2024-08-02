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

module.exports = Rectangle;
