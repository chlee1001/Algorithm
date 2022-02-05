const [N, K] = require('fs').readFileSync('/dev/stdin').toString().trim().split(" ");
const arr = Array.from({length: parseInt(N, 10)}, (_, i) => i + 1);
const result = [];

while (arr.length !== 0) {
    for (let i = 0; i < K - 1; i++) {
        arr.push(arr.shift())
    }
    result.push(arr.shift())
}
console.log(`<${result.join(', ')}>`);