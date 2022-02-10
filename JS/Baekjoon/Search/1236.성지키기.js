/**
 * 백준 1236번 성 지키기
 * 1. 모든 행과 모든 열에 한 명 이상의 경비원이 있어야한다.
 * 2. 행 기준/열 기준으로 필요한 경비원의 수를 각각 계산하여 더 큰 수를 출력한다.
 */

const [size, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const [n, m] = size.split(' ');

const row = new Array(Number(n)).fill(0);
const col = new Array(Number(m)).fill(0);

for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
        if (input[i][j] === 'X') {
            row[i] = 1;
            col[j] = 1;
        }
    }
}

let rowCount = 0;
for (let i = 0; i < n; i++) {
    if (row[i] === 0) {
        rowCount += 1;
    }
}

let colCount = 0;
for (let i = 0; i < m; i++) {
    if (col[i] === 0) {
        colCount += 1;
    }
}
console.log(Math.max(rowCount, colCount));