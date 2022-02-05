// 백준 4195번 친구 네트워크
// 1. 해시를 활용한 Union-Find 알고리즘 이용

const [T, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const resultLog = [];
let parent;
let number;
let F = 0;

/**
 *
 * @param node
 * @returns parent
 *
 * 재귀를 이용하여 현재 노드의 부모의 부모의... 부모를 찾는다
 */
const findParent = (node) => {
    if (node === parent[node]) {
        return parent[node];
    } else {
        parent[node] = findParent(parent[node]);
        return parent[node]
    }
}

/**
 *
 * @param nodeX
 * @param nodeY
 *
 * 두 노드의 부모를 찾고, 부모가 다르면 오른쪽 노드의 부모를 왼쪽 노드로 지정
 * 그리고 오른쪽 노드의 네트워크 크기를 왼쪽으로 더해준다.
 */
const union = (nodeX, nodeY) => {
    let parentX = findParent(nodeX);
    let parentY = findParent(nodeY);

    if (parentX !== parentY) {
        parent[parentY] = parentX;
        number[parentX] += number[parentY]; // x의 네트워크 크기 값에 y의 네트워크 크기값을 더해준다.
    }

}

for (let i = 0; i < T; i++) {
    parent = {};
    number = {};
    F = Number(input[i + F]);

    for (let j = i * (F + 1) + 1; j < (i + 1) * (F + 1); j++) {
        const [nodeX, nodeY] = input[j].split(' ');

        // 부모에 현재 노드가 존재하지 않으면 값을 추가하고, 네트워크 값을 1로 넣어준다.
        if (!(nodeX in parent)) {
            parent[nodeX] = nodeX;
            number[nodeX] = 1;
        }
        if (!(nodeY in parent)) {
            parent[nodeY] = nodeY;
            number[nodeY] = 1;
        }

        union(nodeX, nodeY);
        resultLog.push(number[findParent(nodeX)]);
    }
}
console.log(resultLog.join('\n'));
