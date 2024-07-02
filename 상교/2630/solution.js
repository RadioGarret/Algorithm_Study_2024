const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs
  .readFileSync(root, 'utf8')
  .toString()
  .trim()
  .split('\n')
  .map((ar) => ar.split(' ').map((v) => +v));

const N = parseInt(input.shift());
let blue = 0,
  white = 0;

function square(m, x, y) {
  let first = input[y][x];
  let isUniform = true;
  for (let i = y; i < y + m; i++) {
    for (let j = x; j < x + m; j++) {
      if (input[i][j] !== first) {
        isUniform = false;
        break;
      }
    }
    if (!isUniform) break;
  }

  if (isUniform) {
    first === 0 ? white++ : blue++;
  } else {
    let half = m / 2;
    square(half, x, y);
    square(half, x + half, y);
    square(half, x, y + half);
    square(half, x + half, y + half);
  }
}

square(N, 0, 0);
console.log(white);
console.log(blue);
