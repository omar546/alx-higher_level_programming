#!/usr/bin/node
const pr = require('process');
const filesystem = require('fs');

const file = pr.argv[2];

filesystem.readFile(file, 'utf8', function (err, data) {
  if (err != null) {
    console.log(err);
  } else {
    pr.stdout.write(data);
  }
});
