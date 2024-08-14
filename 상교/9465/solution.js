const fs = require('fs');
const root = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n').map(e=>e.trim());

let T = parseInt(input.shift());
const answer = [];
while (T>0) {

    const N = parseInt(input.shift());
    const arr1 = input.shift().split(' ').map(v=>+v);
    const arr2 = input.shift().split(' ').map(v=>+v);

    const dp = [[0, arr1[0], arr2[0]]];
    for (let i=1; i<N; i++) {
        dp[i] = [
            Math.max(...dp[i-1]),
            Math.max(dp[i-1][0], dp[i-1][2])+arr1[i],
            Math.max(dp[i-1][0], dp[i-1][1])+arr2[i],
        ];
    }
    console.log(Math.max(...dp[N-1]));
    T--;
}
