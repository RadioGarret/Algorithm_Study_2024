const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const N = parseInt(input[0]);

const arr = input[1].split(' ').map((v) => +v);

let answer = 0;
let max = 0;
const dp = Array(N).fill(1);

if (N === 1) {
  console.log(1);
  return;
}

for (let i = 1; i < N; i++) {
  const start = arr[i];
  let partialMax = 1;
  for (let j = 0; j < i; j++) {
    if (arr[j] < start) {
      dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }
}

console.log(Math.max(...dp));
