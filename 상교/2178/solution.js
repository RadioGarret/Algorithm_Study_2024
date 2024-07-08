const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(v=>+v);

const map = input.map(arr=>arr.trim().split('').map(v=>+v));
const visited = Array.from(Array(N), ()=>Array(M).fill(0));
const dx=[1, 0, -1, 0];
const dy=[0, -1, 0, 1];
const queue=[[0,0, 1]];
const answer=[];

function BFS() {
    const [x, y, count] = queue.shift();
    if (x>M-1 || x<0 || y>N-1 | y<0) return;
    if (visited[y][x]==1 || map[y][x] == 0) return;

    if (x==M-1 && y == N-1) {
        answer.push(count);
        return;
    }
    visited[y][x]=1;
    for (let i=0; i<4; i++) {
        queue.push([x+dx[i], y+dy[i], count+1]);
    }
    for (let i=0; i<4; i++){
        BFS();
    }
}

BFS();
console.log(Math.min(...answer));
