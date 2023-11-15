#!/usr/bin/node

let count = 0;

/* simple logging with tracking */
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
