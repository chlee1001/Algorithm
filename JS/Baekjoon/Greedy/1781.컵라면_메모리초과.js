const [N, ...input] = require('fs').
  readFileSync('/dev/stdin').
  toString().
  trim().
  split('\n')

const questions = input.map(data => data.split(' ').map(Number))
const result = []

// 1. 데드라인 수를 기준으로 오름차순 정렬
questions.sort((a, b) => a[0] - b[0])

// 2. 정렬 된 문제의 컵라면을 저장 후, 만약 문제의 개수가 데드라인을 넘으면 최소 원소 제거
for (const question of questions) {
  const [deadline, cupRamen] = question
  result.push(cupRamen)
  result.sort((a, b) => a - b)

  if (result.length > deadline) {
    result.shift()
  }
}

console.log(result.reduce((a, b) => a + b))