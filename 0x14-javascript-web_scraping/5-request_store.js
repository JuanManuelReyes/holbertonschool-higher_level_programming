#!/usr/bin/node
const url = process.argv[2];
const file = process.argv[3];
const axios = require('axios').default;
const fs = require('fs');

axios.get(url).then(function (res) {
  const data = res.data;

  fs.writeFile(file, data, err => {
    if (err) {
      console.error(err);
    }
  });
}).catch(function (error) {
  console.log(`code: ${error.response.status}`);
});
