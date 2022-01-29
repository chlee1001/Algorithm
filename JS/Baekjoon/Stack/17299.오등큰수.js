const [n, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const inputNum = input[0].split(' ').map(num => parseInt(num, 10))
const appearNum = inputNum.reduce((obj, t) => (obj[t] = obj[t] ? obj[t] + 1 : 1, obj), {});
const result = Array(parseInt(n, 10)).fill(-1);

const stackIdx = [];

for (let i = 0; i < n; i++) {
    const base = appearNum[inputNum[i]];
    while (stackIdx.length !== 0 && appearNum[inputNum[stackIdx[stackIdx.length - 1]]] < base) {
        result[stackIdx.pop()] = inputNum[i];
    }
    stackIdx.push(i)

}
console.log(result.join(' '))
