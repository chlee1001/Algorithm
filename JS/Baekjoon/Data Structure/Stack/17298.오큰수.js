const [n, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const inputNum = input[0].split(' ').map(num => parseInt(num, 10))
const result = Array(parseInt(n, 10)).fill(-1);
const stackIdx = [];

for (let i = 0; i < n; i++) {
    const base = inputNum[i];
    while (stackIdx.length !== 0 && inputNum[stackIdx[stackIdx.length - 1]] < base) {
        result[stackIdx.pop()] = base;
    }
    stackIdx.push(i)

}
console.log(result.join(' '))