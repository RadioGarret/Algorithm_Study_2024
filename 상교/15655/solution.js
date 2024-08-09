const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map((v) => +v);
const numbers = input[1]
  .split(' ')
  .map((v) => +v)
  .sort((a, b) => a - b);

const arr = Array(M).fill(0);
const answer = [];
const visited = Array(N).fill(false);

function dfs(count) {
  if (count === M) {
    answer.push(arr.join(' '));
    return;
  }
  for (let i = count; i < N; i++) {
    if (!visited[i]) {
      if (count > 0 && arr[count - 1] > numbers[i]) continue;
      visited[i] = true;
      arr[count] = numbers[i];
      dfs(count + 1);
      visited[i] = false;
    }
  }
}

dfs(0);
console.log(answer.join('\n'));
