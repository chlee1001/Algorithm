// 백준 1920번 수 찾기
// 1. 특정 정수의 등장 여부만을 간단히 체크하면 된다.
// 2. Set 자료형을 이용하면 간단히 풀 수 있다. (집합 -> 중복 x)

const [n, input, m, target] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const inputNum = new Set(input.split(' ').map(num => Number(num)));
const targetNum = target.split(' ').map(num => Number(num));

const result = targetNum.map(num => inputNum.has(num) ? 1 : 0);
console.log(result.join('\n'));
