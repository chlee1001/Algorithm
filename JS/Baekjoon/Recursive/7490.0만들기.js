/**
 * 백준 7490번 0만들기
 * 1. 자여수 N의 범위 (3<=N<=9)가 매우 한정적이므로 완전 탐색으로 문제를 해결할 수 있다.
 * 2. 수의 리스트와 연산자 리스트를 분리하여 모든 경우의 수를 계산한다.
 */
const [T, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

let opList;

function makeOpList(arr, n) {
    if (arr.length === n) {
        opList.push([...arr]);
        return;
    }

    arr.push(' ');
    makeOpList(arr, n);
    arr.pop();

    arr.push('+');
    makeOpList(arr, n);
    arr.pop();

    arr.push('-');
    makeOpList(arr, n);
    arr.pop();

}

for (let i = 0; i < T; i++) {
    const N = Number(input[i]);

    opList = [];
    makeOpList([], N - 1)

    const intList = Array.from({length: N}, (_, i) => i + 1);

    for (const opListElement of opList) {
        let exp = ``;
        for (let j = 0; j < N - 1; j++) {
            exp += intList[j] + opListElement[j];
        }
        exp += intList[intList.length - 1];
        if (eval(exp.replaceAll(' ', '')) === 0) {
            console.log(exp);
        }
    }
    console.log();
}