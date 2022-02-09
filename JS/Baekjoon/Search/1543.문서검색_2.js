/**
 * 백준 1543번 문서검색
 * 1. 문서의 길이는 최대 2,500이고 단어의 길이는 최대 50이다.
 * 2. 단순히 모든 경우의 수를 계산하여 문제를 해결할 수 있다.
 * 3. 시간복잡도 O(NM)의 알고리즘으로 해결할 수 있다.
 */

/**
 * 단순히 전체 문서에서 찾고자는 단어를 기준으로 쪼개면 그 쪼개진 갯수 - 1이 단어의 개수가 된다.
 */

const [doc, target] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const result = doc.split(target);
console.log(result.length - 1);