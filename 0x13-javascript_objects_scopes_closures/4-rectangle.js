#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let lines, Xs;

    for (lines = 0; lines < this.height; lines++) {
      let line = '';
      for (Xs = 0; Xs < this.width; Xs++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    const tempo = this.width;
    this.width = this.height;
    this.height = tempo;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
