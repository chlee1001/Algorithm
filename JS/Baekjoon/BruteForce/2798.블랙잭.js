const [T, input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(T.split(' ')[0])
const M = Number(T.split(' ')[1])

const cards = input.split(' ').map(num => Number(num));

let result = 0;
for (let i = 0; i < N; i++) {
    for (let j = i + 1; j < N; j++) {
        for (let k = j + 1; k < N; k++) {
            let cardSum = cards[i] + cards[j] + cards[k];
            if (result < cardSum && cardSum <= M) {
                result = cardSum
            }
        }
    }
}
console.log(result)