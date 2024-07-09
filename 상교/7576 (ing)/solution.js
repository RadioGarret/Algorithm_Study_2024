const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const [M,N] = input.shift().split(' ').map(v=>+v);

const map = input.map(arr=>arr.trim().split(' ').map(v=>+v));
const minArr = Array.from(Array(N), ()=>Array(M).fill(0));
const dx=[1, 0, -1, 0];
const dy=[0, -1, 0, 1];
const answer=[];
let isAlreadyFull = true;
for (let i=0; i<N; i++) {
    for (let j=0; j<M; j++) {
        if (map[i][j]==1) {
            queue=[[i,j,0]];
            bfs(queue);
        }
        else {
            if (isAlreadyFull) isAlreadyFull = false;
        }
    }
}

if (isAlreadyFull) {
    console.log(0);
    return;
}

function bfs(queue) {
    const [i,j,count] = queue.shift();
    if (i>N-1 || j>M-1 || i<0 || j<0) return;
    if (map[i][j] == -1) return;
    minArr[i][j] = Math.min(count, minArr[i][j]);
    for (let i=0; i<4; i++) {
        queue.push([i+dy, j+dx, count+1]);
        bfs(queue);
    }
}

for (let i=0; i<N; i++) {
    for (let j=0; j<M; j++) {
        if (map[i][j]==0) {
            console.log(-1);
            return;
        }
    }
}