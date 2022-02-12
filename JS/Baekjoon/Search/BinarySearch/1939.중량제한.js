/**
 * 백준 1939번 중량제한
 * 1. 다리의 개수 M의 최대 100,000이며, 중량 제한 C는 최대 1,000,000,000이다.
 * 2. 이진 탐색을 이용하여 O(M*logC)에 문제를 해결할 수 있다.
 * 3. 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 이진 탐색으로 찾는다.
 */

const [NM, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const [N, M] = NM.split(' ').map(num => Number(num));
const bridge = {};
const [departure, dest] = input[M].split(" ").map(Number);


const bfs = (c) => { // 경로 유무 확인
    const queue = [departure];
    let visited = new Array(N + 1).fill(false);
    visited[departure] = true;

    while (queue.length) {
        const cur = queue.shift();
        for (let i = 0; i < bridge[cur].length; i++) {
            const [next, nextCost] = bridge[cur][i];
            if (!visited[next] && nextCost >= c) {
                visited[next] = true;
                queue.push(next)
            }
        }
    }
    return visited[dest];
}

let min = Infinity;
let max = 0;

for (let i = 0; i < M; i++) {
    const [start, end, limit] = input[i].split(' ').map(num => Number(num));
    if (!bridge[start]) bridge[start] = [];
    if (!bridge[end]) bridge[end] = [];
    bridge[start].push([end, limit]);
    bridge[end].push([start, limit]);
    min = Math.min(min, limit);
    max = Math.max(max, limit);
}

let result = min;
while (min <= max) {
    let mid = Math.floor((min + max) / 2);
    if (bfs(mid)) { // 이동가능 -> 중량 증가
        result = mid;
        min = mid + 1;
    } else { // 이동불가 -> 중량 감소
        max = mid - 1
    }
}
console.log(result);