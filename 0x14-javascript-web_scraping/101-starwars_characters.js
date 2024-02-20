#!/usr/bin/node
const process = require('process');
const request = require('request');
let order = [];
let responses = {};

function getCharName (charUrl) {
  let val;
  val = request(charUrl, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      let data = JSON.parse(body);
      val = data['name'];
      responses[charUrl] = val;
    }
  });
}

function doParse () {
  let mov = process.argv[2];
  let getfrom = 'https://swapi-api.alx-tools.com/api/films/' + mov;

  request(getfrom, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      let data = JSON.parse(body);
      data['characters'].forEach(function (charUrl) {
        order.push(charUrl);
        getCharName(charUrl);
      });
    }
  });
}

doParse();
setTimeout(function () {
  order.forEach(function (url) {
    console.log(responses[url]);
  });
}, 5000);
