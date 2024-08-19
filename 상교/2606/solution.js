const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const N = parseInt(input.shift());
const M = parseInt(input.shift());

let graph = [...new Array(N + 1)].map(() => []);
let visited = [...new Array(N + 1).fill(0)];
let ans = 0;

for (let i = 0; i < input.length; i++) {
  let [start, end] = input[i].split(' ').map((v) => +v);

  graph[start].push(end);
  graph[end].push(start);
}

visited[1] = 1;
function dfs(start) {
  for (let end of graph[start]) {
    if (!visited[end]) {
      visited[end] = 1;
      ans++;
      dfs(end);
    }
  }
}
dfs(1);
console.log(ans);
