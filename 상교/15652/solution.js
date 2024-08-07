const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs
  .readFileSync(root, 'utf8')
  .toString()
  .trim()
  .split(' ')
  .map((v) => +v);

const [N, M] = input;

const arr = Array(M).fill(0);
const answer = [];

function dfs(count) {
  if (count === M) {
    answer.push(arr.join(' '));
    return;
  }

  for (let i = 0; i < N; i++) {
    if (count > 0) {
      if (arr[count - 1] > i + 1) {
        continue;
      }
    }
    arr[count] = i + 1;
    dfs(count + 1);
  }
}
dfs(0);
console.log(answer.join('\n'));
