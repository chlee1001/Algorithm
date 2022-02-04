// 백준 5397번 키로거
// 1. 문자열 크기가 최대 1,000,000이므로 시뮬레이션 방식으로는 문제를 해결할 수 없다.
// 2. 스택을 활용하여 선형시간(O(n))문제를 해결할 수 있는 알고리즘을 설계합니다.

const [T, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const resultLog = [];
for (let i = 0; i < T; i++) {
    const testStr = input[i].split('');
    let left = [];
    let right = [];

    for (let j = 0; j < testStr.length; j++) {
        if (testStr[j] === '<') {
            if (left.length > 0) {
                right.push(left.pop())
            }
        } else if (testStr[j] === '>') {
            if (right.length > 0) {
                left.push(right.pop())
            }
        } else if (testStr[j] === '-') {
            if (left.length > 0) {
                left.pop();
            }
        } else {
            left.push(testStr[j]);
        }
    }

    left = left.concat(right.reverse());
    resultLog.push(left.join(''))
}
console.log(resultLog.join('\n'));