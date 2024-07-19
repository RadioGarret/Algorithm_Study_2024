const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const T = parseInt(input.shift());
const answer = [];
for (let i = 0; i < T; i++) {
  const N = parseInt(input[i]);
  const dp = new Array(N + 1).fill(0);
  [dp[1], dp[2], dp[3]] = [1, 1, 1];
  if (N < 4) {
    answer.push(dp[N]);
    continue;
  }
  for (let j = 4; j <= N; j++) {
    dp[j] = dp[j - 2] + dp[j - 3];
  }
  answer.push(dp[N]);
}

console.log(answer.join('\n'));
