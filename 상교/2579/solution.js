const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs
  .readFileSync(root, 'utf8')
  .toString()
  .trim()
  .split('\n')
  .map((v) => +v);

const N = parseInt(input.shift());
input.unshift(0);
let dp = new Array(N + 1).fill(0);

if (N == 1) {
  console.log(input[1]);
  return;
} else if (N == 2) {
  console.log(input[1] + input[2]);
  return;
}

dp[1] = input[1];
dp[2] = input[1] + input[2];

for (let i = 3; i < N + 1; i++) {
  dp[i] = Math.max(
    ...[dp[i - 3] + input[i - 1] + input[i], dp[i - 2] + input[i]],
  );
}

console.log(dp[N]);
