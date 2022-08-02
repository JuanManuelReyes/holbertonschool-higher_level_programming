#!/usr/bin/node
const process = require('process');
const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  let counter = 2;
  let max = 0; const secondMax = 0; let aux = 0;
  while (counter <= argv.length) {
    if (parseInt(argv[counter]) > max) {
      aux = max;
      max = parseInt(argv[counter]);
    } else if (aux > secondMax) {
      secondMax = aux;
    } else if (parseInt(argv[counter]) > secondMax) {
      secondMax = parseInt(argv[counter]);
    }
    counter++;
  }
  console.log(secondMax);
}
