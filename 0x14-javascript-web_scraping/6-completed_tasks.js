#!/usr/bin/node
const process = require('process');
const request = require('request');

let getfrom = process.argv[2];
let data;
let got = {};

request(getfrom, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    data.forEach(function (result) {
      if (result['completed'] === true) {
        let userid = result['userId'];
        if (!(userid in got)) {
          got[userid] = 0;
        }
        got[userid] += 1;
      }
    });
    console.log(got);
  }
});
