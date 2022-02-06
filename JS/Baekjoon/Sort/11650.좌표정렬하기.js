/**
 * 백준 11650번 좌표정렬하기
 * 1. (x좌표, y좌표)를 입력 받은 뒤 x좌표, y좌표 순서대로 차례대로 오르차순 정렬한다.
 */

const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const result = [];
const coords = input.map(coord => coord.split(' ').map(nums => Number(nums)));
coords.sort((a, b) => {
    if (a[0] !== b[0]) {
        return a[0] - b[0];
    }
    return a[1] - b[1];
}).forEach(coord => result.push(`${coord[0]} ${coord[1]}`))

console.log(result.join('\n'));