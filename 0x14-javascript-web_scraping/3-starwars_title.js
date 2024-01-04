#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episode;

// get the body and parse out what we need
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
