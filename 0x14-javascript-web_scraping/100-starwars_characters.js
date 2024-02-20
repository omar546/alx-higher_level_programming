#!/usr/bin/node
const process = require('process');
const request = require('request');

let mov = process.argv[2];
let getfrom = 'https://swapi-api.alx-tools.com/api/films/' + mov;

function printCharName (charUrl) {
  request(charUrl, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      let data = JSON.parse(body);
      console.log(data['name']);
    }
  });
}

request(getfrom, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    let data = JSON.parse(body);
    data['characters'].forEach(function (charUrl) {
      printCharName(charUrl);
    });
  }
});
