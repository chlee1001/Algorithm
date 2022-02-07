/**
 * 백준 2747번 피보나치 수
 * 1. 피보나치 수열의 점화식을 세운다
 *      F0 = 0, F1 = 1
 *      Fn = Fn-1 + Fn-2 (n>=2)
 * 2. 재귀 함수를 이용해 문제를 풀 수 있는지 검토해야 한다.
 * 3. 문제에서 N은 최대 45이다.
 */
const [n] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const Fibo = [];
Fibo[0] = 0;
Fibo[1] = 1;

for (let i = 2; i <= n; i++) {
    Fibo[i] = Fibo[i - 1] + Fibo[i - 2];
}
console.log(Fibo[n]);