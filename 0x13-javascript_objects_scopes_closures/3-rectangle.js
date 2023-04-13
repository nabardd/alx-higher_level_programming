#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.height = undefined;
      this.width = undefined;
    } else {
      this.height = h;
      this.width = w;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      let row = "";
      for (let j = 0; j < this.width; j++) {
        row += "X";
      }
      console.log(row);
    }
  }
}