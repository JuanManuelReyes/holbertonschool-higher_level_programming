#!/usr/bin/node
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const req = require('request');

req.get(url, (err, res) => {
  if (err) {
    console.log('code: ' + err.res.status);
  }
  console.log(res.data.title);
});
