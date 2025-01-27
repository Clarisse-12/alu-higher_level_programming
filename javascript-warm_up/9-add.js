#!/usr/bin/node
function add(a, b) {
  return a + b;
}

const firstInt = parseInt(process.argv[2], 10);
const secondInt = parseInt(process.argv[3], 10);

if (isNaN(firstInt) || isNaN(secondInt)) {
  console.log("NaN");
} else {
  console.log(add(firstInt, secondInt));
}
