const [n, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

console.log(n)
console.log(input)


// const stdin = require('fs').readFileSync('/dev/stdin').toString();
// const [NM, ...input] = stdin.trim().split('\n');
// const [N, M] = NM.split(' ').map(Number);
// const nArr = input.slice(0, N);
// const mArr = input.slice(N, N + M);
//
// const nmMap = new Map();
//
// nArr.forEach((x) => {
//     if (!nmMap.get(x)) {
//         nmMap.set(x, nmMap.get(x) + 1 || 0);
//     }
// });
// mArr.forEach((x) => {
//     if (!nmMap.get(x)) {
//         nmMap.set(x, nmMap.get(x) + 1 || 0);
//     }
// });
//
// const nmArr = [];
// for (let [name, value] of nmMap) {
//     if (value) {
//         nmArr.push(name);
//     }
// }
//
// nmArr.sort();
//
// console.log(nmArr.length);
// console.log(nmArr.join('\n'));
//
