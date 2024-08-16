const fs = require('fs');
const root = process.platform === 'linux' ? '/dev/stdin' : __dirname + ('/input.txt');
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(v=>+v);
const numbers = input[0].split(' ').map(v=>+v).sort((a,b)=>a-b); 
const arr = Array(M).fill(0);
const answer = [];
function dfs(count) {
    if (count===M) {
        answer.push(arr.join(' '));
        return;
    }
    for (let i=0; i<N; i++) {
        arr[count] = numbers[i];
        dfs(count+1);
    }
}
dfs(0);
console.log(answer.join('\n'));