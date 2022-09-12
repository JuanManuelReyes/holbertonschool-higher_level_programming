#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios').default;

axios.get(url).then(function (res) {
  const movies = res.data.results;
  let counter = 0;
  for (let i = 0; i < movies.length; i++) {
    for (let x = 0; x < movies[i].characters.length; x++) {
      if (movies[i].characters[x].includes('18')) {
        counter++; 
        break; 
      }
    }
  }
  console.log(counter);
  }).catch(function (error) {
    console.log(`code: ${error.response.status}`);
});
