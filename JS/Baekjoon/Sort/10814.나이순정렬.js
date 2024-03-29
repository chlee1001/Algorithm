/**
 * 백준 10814번 나이순 정렬
 * 1. (나이, 이름)의 정보를 입력 받은 뒤에 나이를 기준으로 정렬
 * 2. 기본 정렬 알고리즘을 사용하며, 기준을 나이로 설정해야한다.
 */

const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const result = [];
const members = input.map(member => member.split(" "));
members.sort((a, b) => Number(a[0]) - Number(b[0])).forEach(member => result.push(`${member[0]} ${member[1]}`));

console.log(result.join('\n'));

// 단순한 방법
// input.sort((a, b) => parseFloat(a) - parseFloat(b));
// console.log(input.join('\n'));