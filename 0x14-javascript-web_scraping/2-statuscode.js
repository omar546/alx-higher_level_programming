#!/usr/bin/node
const process = require('process');
const request = require('request');

const getfrom = process.argv[2];

request(getfrom, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
