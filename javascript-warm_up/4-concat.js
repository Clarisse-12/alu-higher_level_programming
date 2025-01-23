#!/usr/bin/node
const [, , firstArg = 'undefined', secondArg = 'undefined'] = process.argv;
console.log(`${firstArg} is ${secondArg}`);
