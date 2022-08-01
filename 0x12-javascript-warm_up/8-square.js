#!/usr/bin/node
const arg = parseInt(process.argv[2]);
const char = 'X';

if (isNaN(arg) === false && typeof arg === 'number') {
  for (let i = 0; i < arg; i++) {
    console.log(char.repeat(arg));
  }
} else {
  console.log('Missing size');
}
