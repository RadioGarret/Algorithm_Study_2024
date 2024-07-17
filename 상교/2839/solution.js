const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim();

const N = parseInt(input);
const dp = Array(N+1).fill(-1);

dp[3]=1;
dp[5]=1;

if (N<6) {
  console.log(dp[N]);
  return;
}

for (let i=6; i<=N; i++) {

  if (dp[i-5]!=-1) {
    dp[i]=dp[i-5]+1;
  }
  else if (dp[i-3]!=-1) {
    dp[i]=dp[i-3]+1;
  }
}

console.log(dp[N]);