const [...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let resultLog = '';

for (const inputStr of input) {
    if (inputStr === '.') {
        break;
    }

    const stack = [];
    let flag = 1;

    for (let i = 0; i < inputStr.length; i++) {
        const char = inputStr[i];
        if (char === '(' || char === '[') {
            stack.push(char);
        } else if (char === ')') {
            if (stack.length === 0 || stack[stack.length - 1] === '[') {
                flag = 0;
                break;
            } else if (stack[stack.length - 1] === '(') {
                stack.pop();
            }
        } else if (char === ']') {
            if (stack.length === 0 || stack[stack.length - 1] === '(') {
                flag = 0;
                break;
            } else if (stack[stack.length - 1] === '[') {
                stack.pop();
            }
        }
    }

    if (flag && stack.length === 0) {
        resultLog += 'yes\n';
    } else {
        resultLog += 'no\n';
    }
}

console.log(resultLog);
