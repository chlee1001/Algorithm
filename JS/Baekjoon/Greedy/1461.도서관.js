const [inputNum, ...inputData] = require('fs').
  readFileSync('/dev/stdin').
  toString().
  trim().
  split('\n')

const [N, M] = inputNum.split(' ')
const bookPosition = inputData[0].split(' ').map(data => Number(data))
const positive = []
const negative = []
let result = 0

// 1. 가장 거리가 먼 책까지의 거리
const largest = Math.max(Math.max(...bookPosition), -Math.min(...bookPosition))

// 2.
for (const book of bookPosition) {
  if (book > 0) {
    positive.push(book)
  } else {
    negative.push(-book)
  }
}

// 2. 각 배열 내림차순 정렬
positive.sort((a, b) => b - a)
negative.sort((a, b) => b - a)

// 3. 각 배열 한번에 M개씩 옮길 수 있으므로, 0부터 + M번째의 값 더하기
let idx = 0
while (idx < positive.length) {
  result += positive[idx]
  for (let i = 0; i <= M - 1; i++) {
    idx += 1
  }
}

idx = 0
while (idx < negative.length) {
  result += negative[idx]
  for (let i = 0; i <= M - 1; i++) {
    idx += 1
  }
}
console.log(result * 2 - largest)