#!/usr/bin/node
let file = process.argv[2];
let string = process.argv[3];
const fs = require('fs');

fs.writeFile(file, string, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
});
