/**
 * 백준 1427번 소트인사이드
 * 1. 자릿수를 기준으로 정렬하므로 9부터 0까지 차례대로 확인한다.
 * 2. 각 숫자에 대하여 해당 숫자의 개수를 계산하여 출력한다.
 */

const [input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const resultLog = [];
for (let i = 9; i > -1; i--) {
    for (const inputElement of input) {
        if (Number(inputElement) === i) {
            resultLog.push(i);
        }
    }
}
console.log(resultLog.join(''));

// const inputNums = input.split('').map(num => Number(num));
// const result = inputNums.sort((a, b) => b - a);
// console.log(result.join(''));
