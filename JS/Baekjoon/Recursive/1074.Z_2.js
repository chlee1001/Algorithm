/**
 * 백준 1074번 Z
 * node.js 재귀로 풀면 시간초과 발생...
 * 8 * 8 배열 일 때 각 사분면의 첫번째 값은 0, 16, 32, 48 이다.
 * 4 * 4 배열 일 때 각 사분면의 첫번째 값은 0, 4, 8, 12 이다.
 * 2 * 2 배열 일 때 각 사분면의 첫번째 값은 0, 1, 2, 3 이다.
 * 결국,
 * N * N 배열일 때 각 사분면의 첫번 째 값은
 * (n/2) * (n/2) * 0
 * (n/2) * (n/2) * 1
 * (n/2) * (n/2) * 2
 * (n/2) * (n/2) * 3
 *
 * 그리고 해당 분면 좌표로 이동은 x+=n/2, y+=n/2 이런식으로 간다.
 */

const [input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, r, c] = input.split(' ').map(num => Number(num));
let result = 0;

function solution(n, x, y) {
    let count = 0;

    while (n > 0) {
        n /= 2;

        // 2사분면 (왼쪽 위)
        if (r < x + n && c < y + n) {
            count += 0;
        }
        // 1사분면 (오른쪽 위)
        else if (r < x + n && c >= y + n) {
            count += n * n;
            y += n;
        }
        // 3사분면 (왼쪽 아래)
        else if (r >= x + n && c < y + n) {
            count += n * n * 2;
            x += n; // 해당 분면으로 이동
        }
        // 4사분면
        else {
            count += n * n * 3;
            x += n;
            y += n;
        }
        if (n === 1) {
            console.log(count);
            break;
        }
    }
}

solution(2 ** N, 0, 0);