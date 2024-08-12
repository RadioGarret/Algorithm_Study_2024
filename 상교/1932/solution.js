const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const N = Number(input[0]);
const arr = input.slice(1).map((v) => v.trim().split(' ').map(Number));

const dp = new Array(N).fill(0).map(() => new Array(N).fill(0));
dp[0][0] = arr[0][0];
for (let i = 1; i < N; i++) {
  for (let j = 0; j < i + 1; j++) {
    if (j == 0) {
      dp[i][j] = dp[i - 1][j] + arr[i][j];
    } else if (j == i) {
      dp[i][j] = dp[i - 1][j - 1] + arr[i][j];
    } else dp[i][j] = Math.max(...[dp[i - 1][j - 1], dp[i - 1][j]]) + arr[i][j];
  }
}

console.log(Math.max(...dp[N - 1]));
