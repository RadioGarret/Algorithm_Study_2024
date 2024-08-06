const fs = require('fs');
const root = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split(' ').map(v => +v);

const [N, M] = input;

const arr = Array(M).fill(0);  // M개의 숫자를 선택하기 위한 배열
const visited = Array(N).fill(false);
const answer = [];

function dfs(count) {
    if (count === M) {
        answer.push(arr.join(' '));
        return;
    }
    for (let i=0; i<N; i++) {
        if (!visited[i]){
            visited[i]=true;
            arr[count]=i+1;
            dfs(count+1);
            visited[i]=false;
        }
    }
}

dfs(0);
console.log(answer.join('\n'))