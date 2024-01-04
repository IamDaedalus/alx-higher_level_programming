#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

// use the callback function to handle errors that may arise
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
