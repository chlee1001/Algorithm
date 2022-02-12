/**
 * 백준 2250번 트리의 높이와 너비
 * 1. 중위 순회를 이용하면 X축을 기준으로 왼쪽부터 방문한다는 특징이 있다.
 * 2. 이 문제는 중위 순회 알고리즘을 이용하고, 추가적으로 Level 값을 저장하도록 하여 문제를 해결할 수 있다.
 */

const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const tree = {};
const findRoot = Array.from({length: Number(N) + 1}, () => 0);
for (const string of input) {
    const [parent, left, right] = string.split(" ").map(Number);
    tree[parent] = ([left, right]);
    findRoot[parent] += 1; // 부모노드에 +1
    for (const treeElement of tree[parent]) { // 부모노드에 자식이 있으면, 그 해당 노드에 +1
        if (treeElement !== -1) {
            if (!findRoot[treeElement]) {
                findRoot[treeElement] = 1;
            } else {
                findRoot[treeElement] += 1;
            }
        }
    }
}
const rootNode = findRoot.indexOf(1); // 노드의 카운트가 1인 것 중 첫 번째가 루트노드이다.

// 왼쪽~오른쪽 노드 사이의 너비
let colMinLevel = new Array(Number(N) + 1).fill(Number(N));
let colMaxLevel = new Array(Number(N) + 1).fill(0);
let col = 1;
let depthLevel = 1;
const inOrder = (parent, level) => {
    if (parent === -1) return;
    depthLevel = Math.max(depthLevel, level);
    const [left, right] = tree[parent];

    inOrder(left, level + 1);
    colMinLevel[level] = Math.min(colMinLevel[level], col)
    colMaxLevel[level] = Math.max(colMaxLevel[level], col)
    col += 1;
    inOrder(right, level + 1);
}
inOrder(rootNode, 1);

let resultLevel = 1; // 최종선택 된 깊이레벨
let resultGap = colMaxLevel[0] - colMinLevel[0] + 1; // 간 (가장 오른쪽에 위치한 노드의 열 번호에서 가장 왼쪽에 위치한 노드의 열 번호를 뺀 값 더하기 1로 정의한다)
for (let i = 1; i < depthLevel + 1; i++) {
    const gap = colMaxLevel[i] - colMinLevel[i] + 1;
    if (resultGap < gap) {
        resultLevel = i;
        resultGap = gap;
    }
}

console.log(resultLevel, resultGap);