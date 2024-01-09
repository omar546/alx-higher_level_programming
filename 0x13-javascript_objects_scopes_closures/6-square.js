#!/usr/bin/node
const GrandSquare = require('./5-square');

class Square extends GrandSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let lines, Xs;
    for (lines = 0; lines < this.height; lines++) {
      let line = '';
      for (Xs = 0; Xs < this.width; Xs++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
