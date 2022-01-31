/*
* 우선, 제일 위에 있는 카드를 바닥에 버린다.
* 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
* 예를 들어 N=4인 경우를 생각해 보자.
* 카드는 제일 위에서부터 1234 의 순서로 놓여있다.
* 1을 버리면 234가 남는다.
* 여기서 2를 제일 아래로 옮기면 342가 된다.
* 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다.
* 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
* N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
 */

const [N] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const queue = Array.from({length: parseInt(N, 10)}, (_, i) => i + 1)
let pos = 0;

for (let i = 1; i < N; i++) {
    pos += 1;
    queue.push(queue[pos]);
    pos += 1;
}
console.log(queue[pos])