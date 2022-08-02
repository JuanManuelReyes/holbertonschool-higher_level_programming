#!/usr/bin/node
const array = require('./mains/100-data').list;

const newList = list.map((x, index) => x * index);

console.log(list);
console.log(newList);
