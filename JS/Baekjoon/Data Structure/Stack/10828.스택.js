const [n, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const stack = [];
let resultLog = '';

const outputFunc = (data) => {
    const inputData = data.split(" ");
    const comm = inputData[0];

    switch (comm) {
        case 'push':
            const num = parseInt(inputData[1], 10);
            stack.push(num);
            break;
        case 'pop':
            resultLog += stack.length > 0 ? stack.pop() : -1;
            resultLog += "\n"
            break;
        case 'size':
            resultLog += stack.length;
            resultLog += "\n"
            break;
        case 'empty':
            resultLog += stack.length > 0 ? 0 : 1;
            resultLog += "\n"
            break;
        case 'top':
            resultLog += stack.length > 0 ? stack[stack.length - 1] : -1;
            resultLog += "\n"
            break;
        default:
            break;
    }
}

input.map(data => outputFunc(data))
console.log(resultLog)


