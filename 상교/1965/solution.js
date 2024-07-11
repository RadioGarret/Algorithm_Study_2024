const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const N = parseInt(input.shift());
if (N === 0) {
    console.log(0);
    return;
  }
  

const dp = Array(N).fill(1);
const arr = input[0].split(' ').map(v=>+v);
for (let i=1; i<N; i++) {
    for (let j=0; j<i; j++) {
        if (arr[j] < arr[i]) {
            dp[i] = Math.max(dp[i], dp[j]+1);
        }
    }
}

console.log(Math.max(...dp));