#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const numbers = process.argv.slice(2).map(Number);
  const sortedNumbers = numbers.filter(Number.isInteger).sort((a, b) => b - a);
  if (sortedNumbers.length === 0) {
    console.log(0);
  } else if (sortedNumbers.length === 1) {
    console.log(0);
  } else {
    console.log(sortedNumbers[1]);
  }
}
