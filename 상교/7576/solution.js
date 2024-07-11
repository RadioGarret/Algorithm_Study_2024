const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const [M, N] = input
  .shift()
  .split(' ')
  .map((v) => +v);

const map = input.map((arr) =>
  arr
    .trim()
    .split(' ')
    .map((v) => +v),
);
const visited = Array.from(Array(N), () => Array(M).fill(0));
const dx = [1, 0, -1, 0];
const dy = [0, -1, 0, 1];
const queue = [];

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (map[i][j] === 1) {
      queue.push([i, j]);
    } else if (map[i][j] === 0) {
      visited[i][j] = -1;
    }
  }
}
let head = 0;
while (queue.length > head) {
  const [i, j] = queue[head++];

  for (let k = 0; k < 4; k++) {
    const ni = i + dy[k];
    const nj = j + dx[k];

    if (ni < 0 || ni > N - 1 || nj < 0 || nj > M - 1) continue;
    if (visited[ni][nj] >= 0) continue;
    visited[ni][nj] = visited[i][j] + 1;
    queue.push([ni, nj]);
  }
}
let maxDays = 0;
let isImpossible = false;

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (visited[i][j] === -1) {
      isImpossible = true;
      break;
    }
    maxDays = Math.max(maxDays, visited[i][j]);
  }
  if (isImpossible) break;
}

console.log(isImpossible ? -1 : maxDays);
