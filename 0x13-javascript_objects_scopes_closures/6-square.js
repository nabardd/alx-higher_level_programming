#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c = undefined) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        let row = "";
        for (let j = 0; j < this.size; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}