#!/usr/bin/node
const first = process.argv[2];
const second = process.argv[3];

if (isNaN(first) || isNaN(second)) {
  console.log('NaN');
} else {
  console.log(Number(first) + Number(second));
}
