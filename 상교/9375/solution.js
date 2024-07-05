const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n');

const T = parseInt(input.shift());
let answer = [];

for (let i=0; i<input.length; i++) {
    const N = parseInt(input[i]);
    let dict = {};
    let lengths = [];
    let sum = 1;
    for (let j=1; j<=N; j++) {
        const [item, category] = input[i+j].split(' ').map(a=>a.trim());
        dict[category] ? dict[category].push(item) : dict[category] = [item];
    }
    Object.keys(dict).forEach(e=>lengths.push(dict[e].length));
    lengths.forEach(len => {
        sum *= (len + 1);
      });
    
    answer.push(sum - 1);
    i += N;
}

console.log(answer.join('\n'))
