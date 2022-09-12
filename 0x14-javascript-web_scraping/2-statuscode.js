#!/usr/bin/node
let url = process.argv[2]
const req = require('request');

fs.get(url, (err, res) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code: ' + res.statusCode);
});