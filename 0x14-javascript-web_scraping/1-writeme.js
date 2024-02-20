#!/usr/bin/node
const process = require('process');
const filesystem = require('fs');

let file = process.argv[2];
let input = process.argv[3];

filesystem.writeFile(file, input, 'utf8', function (err, data) {
  if (err != null) {
    console.log(err);
  }
});
