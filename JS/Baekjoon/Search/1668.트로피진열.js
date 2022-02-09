/**
 * 백준 1668번 트로피 진열
 * 1. 선반 위에 올려져 있는 트로피들에 대하여 왼쪽에서, 오른쪽에서 봤을 때 보이는 트로피의 수를 각각 구한다.
 * 2. 트로피의 개수 N이 최대 50이므로 단순 구현
 */

const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const solution = (array) => {
    let result = 1;
    let height = array[0];
    for (let j = 1; j < array.length; j++) {
        const newTrophy = array[j];
        if (height < newTrophy) {
            height = newTrophy;
            result += 1;
        }
    }
    return result;
}

const array = input.map(num => Number(num));

console.log(solution(array));
console.log(solution(array.reverse()));