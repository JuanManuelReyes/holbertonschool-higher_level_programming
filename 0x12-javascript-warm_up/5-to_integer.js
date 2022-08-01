#!/usr/bin/node
const arg = parseInt(process.argv[2]);

if (isNaN(arg) === false && typeof arg === 'number') {
  console.log('My number: ' + arg);
} else {
  console.log('Not a number');
}
