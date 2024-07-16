const fs = require('fs');
const input = fs
  .readFileSync(
    '/Users/sanggyo/Desktop/problem-solve/BOJ/Silver/1927/input.txt',
  )
  .toString()
  .trim()
  .split('\n')
  .map(Number);

const N = input[0];

class minHeap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  push(value) {
    this.heap.push(value);
    let curIdx = this.heap.length - 1;
    let parIdx = Math.floor((curIdx - 1) / 2);
    while (this.heap[parIdx] && this.heap[parIdx] > this.heap[curIdx]) {
      this.swap(curIdx, parIdx);
      curIdx = parIdx;
      parIdx = Math.floor((curIdx - 1) / 2);
    }
  }

  pop() {
    const max = this.heap[0];

    if (this.heap.length == 1) this.heap = [];
    else this.heap[0] = this.heap.pop();

    let curIdx = 0;
    let leftIdx = curIdx * 2 + 1;
    let rightIdx = curIdx * 2 + 2;

    while (
      (this.heap[leftIdx] && this.heap[leftIdx] < this.heap[curIdx]) ||
      (this.heap[rightIdx] && this.heap[rightIdx] < this.heap[curIdx])
    ) {
      let smallerIdx = leftIdx;
      if (this.heap[rightIdx] && this.heap[rightIdx] < this.heap[smallerIdx])
        smallerIdx = rightIdx;
      this.swap(curIdx, smallerIdx);
      curIdx = smallerIdx;
      leftIdx = curIdx * 2 + 1;
      rightIdx = curIdx * 2 + 2;
    }
    return max;
  }
}

let heap = new minHeap();
let answer = [];

for (let i = 1; i < N + 1; i++) {
  if (input[i] === 0) {
    if (heap.size() <= 0) answer.push(0);
    else answer.push(heap.pop());
  } else heap.push(input[i]);
}

console.log(answer.join('\n'));
