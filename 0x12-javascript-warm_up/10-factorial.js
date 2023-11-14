#!/usr/bin/node
const num = process.argv[2];

function factorial (number) {
  if (isNaN(number) || number <= 0) {
    return 1;
  }

  return number * factorial(number - 1);
}

console.log(factorial(num));
