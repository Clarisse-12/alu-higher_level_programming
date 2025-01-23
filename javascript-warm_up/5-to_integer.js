#!/usr/bin/node
const [, , firstArg] = process.argv;
const number = Number.parseInt(firstArg, 10);
console.log(Number.isNaN(number) ? 'Not a number' : `My number: ${number}`);
