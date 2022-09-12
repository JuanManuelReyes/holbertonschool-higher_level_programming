#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios').default;

axios.get(url).then(function (res) {
  const data = res.data;
  const dict = {};
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed === true) {
      if (dict[data[i].userId] !== undefined) {
        dict[data[i].userId] = dict[data[i].userId] += 1;
      } else {
        dict[data[i].userId] = 1;
      }
    }
  }
  console.log(dict);
}).catch(function (error) {
  console.log(`code: ${error.response.status}`);
});
