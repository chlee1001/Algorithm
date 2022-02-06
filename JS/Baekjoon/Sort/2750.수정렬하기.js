/**
 * 백준 2750번 수 정렬하기
 * 1. 데이터의 개수가 1,000개 이하이므로 기본적인 정렬 알고리즘으로 해결가능
 */

const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

inputNums = input.map(num => Number(num));
const result = inputNums.sort((a, b) => a - b);

console.log(result.join('\n'));