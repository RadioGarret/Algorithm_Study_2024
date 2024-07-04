const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');
const [N, M] = input
  .shift()
  .split(' ')
  .map((v) => +v);

let checked = new Array(N + 1).fill(0);
let adjList = {};
let answer = 0;
let count = 0;
for (let i = 0; i < M; i++) {
  const [s, e] = input[i].split(' ').map((v) => +v);
  adjList[s] ? adjList[s].push(e) : (adjList[s] = [e]);
  adjList[e] ? adjList[e].push(s) : (adjList[e] = [s]);
}

function dfs(v) {
  if (checked[v]) return;
  checked[v] = 1;
  count++;

  adjList[v].forEach((el) => {
    if (!checked[el]) dfs(el);
  });
}

for (let i = 1; i <= N; i++) {
  if (checked[i] === 0) {
    if (adjList[i]) {
      count = 0;
      dfs(i);
      if (count > 0) answer++;
    } else {
      answer++;
    }
  }
}

console.log(answer);
