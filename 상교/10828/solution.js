const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

let n = Number(input[0]);
let arr = [];
let answer = [];

const foo = {
  top: () => {
    arr.length > 0 ? answer.push(arr[arr.length - 1]) : answer.push(-1);
  },
  size: () => {
    answer.push(arr.length);
  },
  empty: () => {
    arr.length > 0 ? answer.push(0) : answer.push(1);
  },
  pop: () => {
    arr.length > 0
      ? answer.push(arr.splice(arr.length - 1, 1)[0])
      : answer.push(-1);
  },
};

for (let i = 0; i < n; i++) {
  const command = input[i + 1].split(' ');
  command[0] === 'push' ? arr.push(command[1]) : foo[command[0]]();
}

console.log(answer.join('\n'));
