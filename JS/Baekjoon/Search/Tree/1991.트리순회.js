const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const tree = {};
const result = [];
for (const string of input) {
    const [root, left, right] = string.split(" ");
    tree[root] = ([left, right]);
}

const preOrder = (root) => {
    if (root === '.') {
        return;
    }
    const [left, right] = tree[root];
    result.push(root);
    preOrder(left);
    preOrder(right);

}
const inOrder = (root) => {
    if (root === '.') {
        return;
    }
    const [left, right] = tree[root];
    inOrder(left);
    result.push(root);
    inOrder(right);

}
const postOrder = (root) => {
    if (root === '.') {
        return;
    }
    const [left, right] = tree[root];
    postOrder(left);
    postOrder(right);
    result.push(root);

}

preOrder('A');
result.push('\n');
inOrder('A');
result.push('\n');
postOrder('A');
console.log(result.join(''))