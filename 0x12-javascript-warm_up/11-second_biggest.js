#!/usr/bin/node
const args = process.argv;

if (args.length > 3) {
  console.log(Number(args.sort().reverse()[1]));
}
