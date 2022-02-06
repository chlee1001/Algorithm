/**
 * 백준 10989번 수 정렬하기3
 * 1. 데이터의 개수가 최대 10,000,000개이다.
 * 2. 시간 복잡도 O(N)의 정렬 알고리즘을 이용해야한다.
 * 3. 수의 범위가 1 ~ 10,000이므로 계수 정렬을 이용할 수 있다.
 */

const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const result = [];
const array = new Array(10001).fill(0);

input.map(num => array[Number(num)] += 1);

array.forEach((num, idx) => {
    if (num !== 0) {
        for (let i = 0; i < num; i++) {
            result.push(idx);
        }
    }
})
console.log(result.join('\n'));


