const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const [N, M] = input
  .shift()
  .split(' ')
  .map((v) => +v);

const answer = [];

input.sort();

for (let i = 1; i < N + M; i++) {
  if (input[i] == input[i - 1]) answer.push(input[i]);
}

console.log(answer.length);
console.log(answer.join('\n'));
