const fs = require('fs');
const root = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n').map(e => e.trim());

const N = parseInt(input.shift());
const adj = Array.from({ length: N + 1 }, () => []);
const parent = Array(N + 1).fill(null);

// 무방향 그래프 (트리) 구성
for (let i = 0; i < N - 1; i++) {
  const [u, v] = input[i].split(' ').map(Number);
  adj[u].push(v);
  adj[v].push(u);
}

// BFS로 부모 찾기
const queue = [1]; // 루트 노드는 1로 설정
parent[1] = 0; // 루트의 부모는 0 (또는 null)로 설정

while (queue.length > 0) {
  const node = queue.shift();
  
  for (let neighbor of adj[node]) {
    if (parent[neighbor] === null) { // 아직 부모가 없는 경우
      parent[neighbor] = node; // 부모 설정
      queue.push(neighbor);
    }
  }
}

// 부모 노드 출력 (루트 노드 제외)
let answer = '';
for (let i = 2; i <= N; i++) {
  answer += parent[i] + '\n';
}

console.log(answer.trim());
