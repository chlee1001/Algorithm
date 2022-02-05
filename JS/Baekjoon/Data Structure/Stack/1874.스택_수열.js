const [n, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const stack = []
let resultLog = '';

let curNum = 1;
let flag = 1;

for (let i = 0; i < n; i++) {
    const targetNum = parseInt(input[i], 10);
    while (curNum <= targetNum) {
        stack.push(curNum);
        resultLog += "+\n"
        curNum += 1;
    }
    if (stack[stack.length - 1] === targetNum) {
        stack.pop()
        resultLog += "-\n"
    } else {
        console.log("NO")
        flag = 0;
        break;
    }
}

if (flag) {
    console.log(resultLog)
}