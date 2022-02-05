// 백준 1874번 스택수열
// 1. 스택에 원소를 삽입할 때는, 단순히 특정 수에 도달할 때까지 삽입하면 된다.
// 2. 스택에서 원소를 연달아 빼낼 때 내림차순을 유지할 수 잇는지 확인한다.

const [n, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const stack = [];
let flag = true;
let num = 1;

let resultLog = '';

for (let i = 0; i < n; i++) {
    while (num <= Number(input[i])) { // 입력 받은 데이터에 도달할 때까지 삽입
        stack.push(num);
        resultLog += '+\n';
        num += 1;
    }
    if (stack[stack.length - 1] === Number(input[i])) { // 스택의 최상위 원소가 데이터와 같을 때 출력
        stack.pop();
        resultLog += '-\n';
    } else { // 내림차순 불가능한 경우
        console.log('NO');
        flag = false;
        break;
    }
}
if (flag) {
    console.log(resultLog);
}