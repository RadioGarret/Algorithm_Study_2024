const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs
  .readFileSync(root, 'utf8')
  .toString()
  .trim()
  .split('\n')

const [N, M] = input[0].split(' ').map(v=>+v);
const numbers = input[1].split(' ').map(v=>+v).sort( (a,b) => a-b);

const arr = Array(M).fill(0);
const visited = Array(N).fill(false);
const answer = [];

function dfs(count) {
  if (count===M) {
    answer.push(arr.join(' '));
    return;
  }

  for (let i=0; i<N; i++) {
    if (!visited[i]){
      visited[i]=true;
      arr[count]=numbers[i];
      dfs(count+1);
      visited[i]=false;
    }
  }
}
dfs(0);
console.log(answer.join('\n'));