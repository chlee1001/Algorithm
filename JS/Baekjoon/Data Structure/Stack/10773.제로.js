const [k, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const stack = [];

const outputFunc = (data) => {
    const num = parseInt(data, 10);
    if (num > 0) {
        stack.push(num)
    } else {
        stack.pop()
    }
}

input.map(data => outputFunc(data));

const resultSum = stack.concat([0]).reduce((prev, cur) => prev + cur)
console.log(resultSum)