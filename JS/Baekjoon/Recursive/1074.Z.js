/**
 * 백준 1074번 Z
 * node.js 시간초과 알고리즘
 */

const [input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, r, c] = input.split(' ').map(num => Number(num));
let result = 0;

function solution(n, x, y) {
    if (n === 2) {
        if (x === r && y === c) {
            console.log(result);
            return;
        }
        result += 1;
        if (x + 1 === r && y === c) {
            console.log(result);
            return;
        }
        result += 1;
        if (x === r && y + 1 === c) {
            console.log(result);
            return;
        }
        result += 1;
        if (x + 1 === r && y + 1 === c) {
            console.log(result);
            return;
        }
        result += 1;
        return;
    }
    solution(n / 2, x, y);
    solution(n / 2, x, y + n / 2);
    solution(n / 2, x + n / 2, y);
    solution(n / 2, x + n / 2, y + n / 2);
}

solution(2 ** N, 0, 0);