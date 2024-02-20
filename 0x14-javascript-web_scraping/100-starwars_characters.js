#!/usr/bin/node
const process = require('process');
const request = require('request');

const mov = process.argv[2];
const getfrom = 'https://swapi-api.alx-tools.com/api/films/' + mov;

function printCharName (charUrl) {
  request(charUrl, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      console.log(data.name);
    }
  });
}

request(getfrom, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.characters.forEach(function (charUrl) {
      printCharName(charUrl);
    });
  }
});
