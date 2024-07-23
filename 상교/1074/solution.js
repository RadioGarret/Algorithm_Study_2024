const fs = require('fs');
const root = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split(' ').map(v => +v);

let [N, r, c] = input;
let answer = 0;

for (let i = N - 1; i >= 0; i--) {
    let half = 1 << i; 
    let quadrantSize = half * half;

    if (r < half && c < half) {
    } else if (r < half && c >= half) {
        answer += quadrantSize;
        c -= half; 
    } else if (r >= half && c < half) {
        answer += 2 * quadrantSize;
        r -= half; 
    } else {
        answer += 3 * quadrantSize;
        r -= half;
        c -= half;
    }
}

console.log(answer);
