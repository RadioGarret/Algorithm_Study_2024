const fs = require('fs');
const root = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split(' ').map(v=>+v);

const [N, M] = input;

const arr = Array(N).fill(0);
const visited = Array(N).fill(0);
let answer=[];


function dfs(num, count) {
    if (count==M) {
        let ans = '';
        for (let i=0; i<M; i++) {
            ans += arr[i];
            ans += ' ';
        }
        answer.push(ans);
    }
    for (let i = num; i<=N; i++) {
        if (!visited[i]) {
            visited[i] = 1;
            arr[count] = i;
            dfs(i+1, count+1);
            visited[i]=0;
        }
    }
}

dfs(1,0);
console.log(answer.join('\n'));