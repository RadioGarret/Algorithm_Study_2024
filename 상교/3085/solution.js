const fs = require('fs');
const root = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const N = parseInt(input.shift());
const arr = input.map(e => e.trim().split(''));
let max = 0;

if (N === 1) {
    console.log(1);
    return;
}

const checkMaxSequence = (arr, N) => {
    let max = 0;
    
    // 각 셀에 대해 가로 방향 시퀀스 검사
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (j < N - 1) {
                // 가로로 인접한 셀과 교환
                [arr[i][j], arr[i][j+1]] = [arr[i][j+1], arr[i][j]];
                max = Math.max(max, findMaxLength(arr, N));
                // 원래 상태로 복구
                [arr[i][j], arr[i][j+1]] = [arr[i][j+1], arr[i][j]];
            }
            if (i < N - 1) {
                // 세로로 인접한 셀과 교환
                [arr[i][j], arr[i+1][j]] = [arr[i+1][j], arr[i][j]];
                max = Math.max(max, findMaxLength(arr, N));
                // 원래 상태로 복구
                [arr[i][j], arr[i+1][j]] = [arr[i+1][j], arr[i][j]];
            }
        }
    }
    
    return max;
};

const findMaxLength = (arr, N) => {
    let maxLen = 1;
    
    // 가로 방향 최대 길이 찾기
    for (let i = 0; i < N; i++) {
        let len = 1;
        for (let j = 1; j < N; j++) {
            if (arr[i][j] === arr[i][j - 1]) {
                len++;
                maxLen = Math.max(maxLen, len);
            } else {
                len = 1;
            }
        }
    }
    
    // 세로 방향 최대 길이 찾기
    for (let j = 0; j < N; j++) {
        let len = 1;
        for (let i = 1; i < N; i++) {
            if (arr[i][j] === arr[i - 1][j]) {
                len++;
                maxLen = Math.max(maxLen, len);
            } else {
                len = 1;
            }
        }
    }
    
    return maxLen;
};

const result = checkMaxSequence(arr, N);
console.log(result);
