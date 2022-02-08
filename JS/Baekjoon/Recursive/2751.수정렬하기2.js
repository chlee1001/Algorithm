/**
 * 백준 2751번 수 정렬하기2
 * 1. 데잍의 개수가 최대 1,000,000개이다.
 * 2. 시간복잡도 O(NlogN)의 정렬 알고리즘을 이용해야한다.
 * 3. 고급 정렬 알고리즘 (Merge, Quick, Heap 정렬 등)을 이ㅛㅇ해야 문제를 해결할 수 있따.
 * 4. 혹은 기본정렬 라이브러리를 이용하면 될 수도 있다.
 *    자바스크립트는 브라우저마다 사용하는 정렬종류가 다르다고 함 (https://ichi.pro/ko/60-cho-an-e-jeonglyeol-jeonglyeol-e-daehan-ppaleun-javascript-inteobyu-dabbyeon-189902715005090)
 *    Node.js에서의 기본 정렬 또한 Merge나 Quick보다 느리다고 함. (https://remocon33.tistory.com/668)
 */

const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const numList = input.map(num => Number(num)).sort((a, b) => a - b);
console.log(numList.join('\n'));
