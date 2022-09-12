#!/usr/bin/node

/*
https://www.geeksforgeeks.org/node-js-process-argv-property/#:~:text=argv%20property%20is%20an%20inbuilt,run%20in%20the%20command%20line.&text=Return%20Value%3A%20This%20property%20returns,it%20in%20the%20command%20line.
https://nodejs.dev/en/learn/reading-files-with-nodejs/

*/
let file = process.argv[2]
const fs = require('fs');

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
