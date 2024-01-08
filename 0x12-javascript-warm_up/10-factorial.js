#!/usr/bin/node
function factorial (p) {
  if (p === 0 || isNaN(p)) {
    return (1);
  }

  if (p < 0) {
    return (-1);
  }

  return (p * factorial(p - 1));
}
console.log(factorial(Number(process.argv[2])));
