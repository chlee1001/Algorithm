/**
 * 백준 1439번 뒤집기
 *
 * 문자열에 잇는 숫자를 모두 0혹은 모두 1로 만들어야한다.
 * 1) 모두 1로 만드는 경우
 *    첫 번째 원소가 0인 경우,
 *    2개씩 원소를 비교할 때, 1에서 0으로 바뀌는 경우
 */

const [...input] = require('fs').
  readFileSync('/dev/stdin').
  toString().
  trim().
  split('\n')

const numStr = input[0].split('')
let count0 = 0 // 0으로 바꾸는 횟수
let count1 = 0 // 1로 바꾸는 횟수

if (numStr[0] === '0') count1 += 1
else count0 += 1

for (let i = 0; i < numStr.length - 1; i++) {
  if (numStr[i] !== numStr[i + 1]) {
    if (numStr[i + 1] === '0') count1 += 1
    else count0 += 1
  }
}
console.log(Math.min(count0, count1))