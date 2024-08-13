const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
let input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const N = parseInt(input.shift());
const M = parseInt(input.shift());
const [start, end] = input.pop().split(' ').map(v=>+v);
input = input.map((v)=>v.split(" ").map(Number));

const graph = Array.from({length: N+1}, ()=>[]);
for (let [s, e, v] of input) {
    graph[s].push({node:e, cost:v});
}

const dist = Array(N+1).fill(Infinity);
const visited = Array(N+1).fill(false);

function findSmallestNode() {
    let min_dist = Infinity;
    let min_node = 0;
    for (let i=0; i<=N; i++) {
        if (!visited[i] && dist[i] < min_dist) {
            min_dist = dist[i];
            min_node = i;
        }
    }
    return min_node;
}

function dijkstra() {
    dist[start] = 0;
    visited[start] = true;
    graph[start].forEach((next)=> {
        dist[next.node] = Math.min(dist[next.node], next.cost);
    });
    for (let i = 1; i<=N; i++) {
        let now_node = findSmallestNode();
        visited[now_node] = true;

        graph[now_node].forEach((next)=> {
            const acc = dist[now_node]+next.cost;
            if (acc<dist[next.node] && !visited[next.node]) {
                dist[next.node] = acc;
            }
        })
    }
}

dijkstra();
console.log(dist[end]-dist[start]);