const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const result = [];
const bookList = input.sort();

for (let i = 0; i < Number(N); i++) {
    const book = bookList[i];
    if (Object.keys(result).includes(book)) {
        result[book] += 1;
    } else {
        result[book] = 1;
    }
}
const maxNum = Math.max(...Object.values(result));
const bestSeller = Object.keys(result).find(key => result[key] === maxNum);
console.log(bestSeller)