const fs = require('fs');
const root =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(root, 'utf8').toString().trim().split('\n').map(e=>e.trim());

const N = parseInt(input.shift());
const preGraph = {};
const midGraph = {};
const postGraph = {};

const preVisited = [];
const midVisited = [];

const answer = [];

let preAns='';
let midAns='';
let postAns='';

for (let i=0; i<N; i++){
    let [root, left, right] = input[i].split(' ');
    preGraph[root] = {left: left, right: right};
    midGraph[root] = {left: left, right: right};
    postGraph[root] = {left: left, right: right};
    preVisited[root] = false;
    midVisited[root] = false;
}

function pre(alphabet) {
    if (preGraph[alphabet].left != '.') {
        if (!preVisited[alphabet]) {
            preAns+=alphabet;
            preVisited[alphabet] = true;
        }
        pre(preGraph[alphabet].left);

    }
    if (preGraph[alphabet].right != '.') {
        if (!preVisited[alphabet]) {
            preAns+=alphabet;
            preVisited[alphabet]=true;
        }
        pre(preGraph[alphabet].right);

    }
    if (postGraph[alphabet].left === '.' && postGraph[alphabet].right === '.') {
        preAns+=alphabet;
        return;
    }
}
pre('A')
answer.push(preAns);

function mid(alphabet) {
    if (!midVisited[alphabet].left && midGraph[alphabet].left != '.') {
        mid(midGraph[alphabet].left);
    }
    midVisited[alphabet] = true;
    midAns+=alphabet;

    if (!midVisited[alphabet].right && midGraph[alphabet].right != '.') {
        mid(midGraph[alphabet].right);
    }
}
mid('A');
answer.push(midAns);

function post(alphabet) { 
    if (postGraph[alphabet].left != '.') {
        const result = post(postGraph[alphabet].left);
        if (result===-1) postGraph[alphabet].left='.';
    }
    if (postGraph[alphabet].right !='.') {
        const result = post(postGraph[alphabet].right);
        if (result===-1) postGraph[alphabet].right='.';
    }
    if (postGraph[alphabet].left === '.' && postGraph[alphabet].right === '.') {
        postAns+=alphabet;
        return -1;
    }
}
post('A');
answer.push(postAns);


console.log(answer.join('\n'))
