const fs = require('fs');
const root = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const N = parseInt(input.shift());
const numbers = input[0].split(' ').map(v => +v);

let maxLen = 0;
let left = 0;
let right = 0;
const countMap = new Map();

while (right < N) {
    countMap.set(numbers[right], (countMap.get(numbers[right]) || 0) + 1);
    
    while (countMap.size > 2) {
        countMap.set(numbers[left], countMap.get(numbers[left]) - 1);
        if (countMap.get(numbers[left]) === 0) {
            countMap.delete(numbers[left]);
        }
        left++;
    }
    
    maxLen = Math.max(maxLen, right - left + 1);
    right++;
}

console.log(maxLen);
