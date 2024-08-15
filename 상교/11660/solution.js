const fs = require('fs');
const root = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');
const [N, M] = input.shift().split(' ').map(v=>+v);

const arr = [];
const answer = [];
for (let i=0; i<N; i++) {
    arr.push(input[i].split(' ').map(v=>+v));
}
const vertSums = Array.from({ length: N }, () => Array(N).fill(0));

for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        vertSums[i][j] = arr[i][j] + (i > 0 ? vertSums[i - 1][j] : 0);
    }
}
for (let i=N; i<N+M; i++) {
    const [x1, y1, x2, y2] = input[i].split(' ').map(v=>+v);

    let sum = 0;
    for (let j=y1-1; j<=y2-1; j++) {
        sum+=vertSums[x2-1][j]- (x1 > 1 ? vertSums[x1 - 2][j] : 0);
    }
    answer.push(sum);
}
console.log(answer.join('\n'));