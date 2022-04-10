class MaxHeap {
  constructor () {
    this.heap = []
  }

  swap (a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]]
  }

  size () {
    return this.heap.length
  }

  push (value) {
    this.heap.push(value)
    let current = this.heap.length - 1
    let parent = Math.floor((current - 1) / 2)

    while (this.heap[parent] < value) {
      this.swap(parent, current)
      current = parent
      parent = Math.floor((current - 1) / 2)
    }
  }

  pop () {
    const last = this.heap.length - 1
    let current = 0
    this.swap(current, last)
    const value = this.heap.pop()

    while (current < last) {
      let left = current * 2 + 1
      let right = current * 2 + 2

      if (left >= last) {
        break
      } else if (right >= last) {
        if (this.heap[current] < this.heap[left]) {
          this.swap(current, left)
          current = left
        } else {
          break
        }
      } else {
        if (this.heap[left] > this.heap[current] || this.heap[right] >
          this.heap[current]) {
          let next = this.heap[left] > this.heap[right] ? left : right
          this.swap(current, next)
          current = next
        } else {
          break
        }
      }
    }
    return value
  }
}

const fs = require('fs')
const input = fs.readFileSync('./dev/stdin').
  toString().
  trim().
  split('\n').
  map(v => v.split(' ').map(Number))
const [N] = input.shift()
if (N === 0) {
  process.exit(console.log(0))
}

let answer = 0
const problem = input.sort((a, b) => b[0] - a[0])
let day = problem[0][0]
let pq = new MaxHeap()

for (let i = 0; i < N; i++) {
  if (day === problem[i][0]) {
    pq.push(problem[i][1])
  } else {
    while (problem[i][0] < day) {
      if (pq.size()) answer += pq.pop()
      day--
    }
    pq.push(problem[i][1])
  }
}

while (day > 0) {
  if (pq.size()) answer += pq.pop()
  day--
}

console.log(answer)
