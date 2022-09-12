#!/usr/bin/node
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const axios = require('axios');

axios.get(url).then(res => {
  console.log(res.data.title);
}).catch(err => {
  console.log('code: ' + err.res.status);
})
