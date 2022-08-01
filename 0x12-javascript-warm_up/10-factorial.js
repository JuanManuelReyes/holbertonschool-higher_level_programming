#!/usr/bin/node
function factorial (num) {
  if (num < 2) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

const arg = parseInt(process.argv[2]);

if (isNaN(arg) === false && typeof arg === 'number') {
  const res = factorial(arg);
  console.log(res);
} else {
  console.log(1);
}
