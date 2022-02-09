/**
 * 백준 1543번 문서검색
 * 1. 문서의 길이는 최대 2,500이고 단어의 길이는 최대 50이다.
 * 2. 단순히 모든 경우의 수를 계산하여 문제를 해결할 수 있다.
 * 3. 시간복잡도 O(NM)의 알고리즘으로 해결할 수 있다.
 */

const [doc, target] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

let count = 0;
let idx = 0;

while (idx + target.length <= doc.length) {
    let tempWord = '';
    for (let j = idx; j < idx + target.length; j++) {
        tempWord += doc[j];
    }
    if (tempWord === target) {
        count += 1;
        idx += target.length;
    } else {
        idx += 1;
    }
}
console.log(count);