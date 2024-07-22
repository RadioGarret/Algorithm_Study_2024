const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs
  .readFileSync(root, 'utf8')
  .toString()
  .trim()
  .split('\n').map(v=>+v)

const N = parseInt(input.shift());

input.sort((a,b)=>a-b);
let answer=0;

for (let i=0; i<N; i++) {
    if (input[i] != i+1) {
        answer+=Math.abs(input[i]-(i+1));
    }
}

console.log(answer);