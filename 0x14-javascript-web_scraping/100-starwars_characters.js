#!/usr/bin/node
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const axios = require('axios').default;

axios.get(url).then(res => {
  for (const char in res.data.characters) {
    axios.get(res.data.characters[char]).then(res => {
              console.log(res.data.name);
            });
        }
  }).catch(function (error) {
    console.log(`code: ${error.res.status}`);
  });
  