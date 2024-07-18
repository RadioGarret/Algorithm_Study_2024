const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim();

const N = parseInt(input);
const dp = Array(N + 1).fill(0);
dp[0] = 0;
dp[1] = 1;
dp[2] = 3;
for (let i = 3; i <= N; i++) {
  dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007;
}

console.log(dp[N]);
