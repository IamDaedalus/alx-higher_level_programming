#!/usr/bin/node
const args = process.argv;

if (args.length > 3) {
  console.log(args.sort().reverse()[1]);
}
