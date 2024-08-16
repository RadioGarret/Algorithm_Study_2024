const fs = require('fs')
const root = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n').map(e=>e.trim());
const N = input[0].length;
const M = input[1].length;
const str1 = ['1', ...input[0].split('')];
const str2 = ['2', ...input[1].split('')];
const lcs = Array.from({length:N+1}, ()=>new Array(M+1).fill(0));
let max = 0;

for (let i=1; i<N+1; i++) {
    for (let j=1; j<M+1; j++) {
        if (str1[i] == str2[j]) {
            lcs[i][j] = lcs[i-1][j-1]+1;
        }
        else {
            lcs[i][j] = Math.max(lcs[i-1][j], lcs[i][j-1]);
        }
    }
}

console.log(lcs[N][M]);