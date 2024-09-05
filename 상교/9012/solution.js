const fs = require('fs');
const input = fs
  .readFileSync(
    '/Users/sanggyo/Desktop/problem-solve/BOJ/Silver/9012/input.txt',
  )
  .toString()
  .trim()
  .split('\n');

const N = Number(input[0]);
let answer = [];

for (let i = 0; i < N; i++) {
  let count = 0;
  const arr = input[i + 1].split('');
  for (let j = 0; j < arr.length; j++) {
    if (arr[j] === '(') {
      count++;
    } else count--;

    if (count < 0) {
      answer.push('NO');
      break;
    }
  }
  if (count === 0) answer.push('YES');
  else if (count > 0) answer.push('NO');
}

console.log(answer.join('\n'));
