/**
 * 백준 2110번 공유기 설치
 * 1. 집의 개수 N의 최대 200,000이며, 집의 좌표 X는 최대 1,000,000,000이다.
 * 2. 이진 탐색을 이용하여 O(N*logX)에 문제를 해결할 수 있다.
 * 3. 가장 인접한 두 공유기 사이의 최대 Gap을 이진 탐색으로 찾는다.
 */

const [NC, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const [N, C] = NC.split(" ").map(num => Number(num));
const houses = input.map(house => Number(house)).sort((a, b) => a - b);

// 두 집 사이의  Min, Max 거리를 찾아 시작, 끝 지점으로 할당
let start = 1;
let end = houses[houses.length - 1] - houses[0];
let result = 0;

// 두 집사이의 거리가 같아질 때 까지
while (start <= end) {
    const mid = Math.floor((start + end) / 2); // 공유기를 설치할 간격
    let setValue = houses[0];
    let count = 1;

    for (let i = 1; i < houses.length; i++) {
        if (houses[i] >= setValue + mid) {
            setValue = houses[i];
            count += 1;
        }
    }
    if (count >= C) {
        start = mid + 1;
        result = mid;
    } else {
        end = mid - 1;
    }

}
console.log(result);

