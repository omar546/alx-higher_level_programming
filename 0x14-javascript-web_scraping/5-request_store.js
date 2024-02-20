#!/usr/bin/node
const process = require('process');
const request = require('request');
const filesystem = require('fs');

const getfrom = process.argv[2];
const filepath = process.argv[3];

request(getfrom, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    filesystem.writeFile(filepath, body, 'utf8', function (err, data) {
      if (err != null) {
        console.log(error);
      }
    });
  }
});
