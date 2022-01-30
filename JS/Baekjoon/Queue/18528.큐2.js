const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const queue = []
let resultLog = '';
let pos = 0;
const outputFunc = (inputData) => {
    const data = inputData.split(' ');

    switch (data[0]) {
        case 'push':
            queue.push(parseInt(data[1], 10))
            break;
        case 'pop':
            if (queue.length - pos === 0) {
                resultLog += `-1\n`
            } else {
                // resultLog += `${queue.shift()}\n`
                resultLog += `${queue[pos]}\n`
                pos += 1;
            }
            break;
        case 'size':
            resultLog += `${queue.length - pos}\n`
            break;
        case 'empty':
            if (queue.length - pos === 0) {
                resultLog += `1\n`
            } else {
                resultLog += '0\n'
            }
            break;
        case 'front':
            if (queue.length - pos === 0) {
                resultLog += '-1\n'
            } else {
                resultLog += `${queue[pos]}\n`
            }
            break;
        case 'back':
            if (queue.length - pos === 0) {
                resultLog += '-1\n'
            } else {
                resultLog += `${queue[queue.length - 1]}\n`
            }
            break;
        default:
            break;
    }
}

for (let i = 0; i < N; i++) {
    outputFunc(input[i]);
}
console.log(resultLog)