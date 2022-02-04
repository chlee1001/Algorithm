// 백준 1966번 프린터큐
// 1. 데이터의 개수(N<=100)가 많지 않으므로, 단순히 문제에서 요구하는 대로 구현
// 2. 현재 리스트에서 가장 큰 수가 앞에 올 때까지 회전시킨 뒤에 추출
// 3. 가장 큰 수가 M이면서 가장 앞에 있을 때 종료

const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const resultLog = [];

for (let i = 0; i < N * 2; i += 2) {
    let [N, M] = input[i].split(" ").map(num => parseInt(num, 10));
    const docList = input[i + 1].split(" ").map((num, idx) => [parseInt(num, 10), idx]);

    let count = 0;

    while ((docList.length !== 0)) {
        let maxValue = Math.max(...docList.map(num => num[0]))

        if (docList[0][0] === maxValue) {
            count += 1;
            if (docList[0][1] === M) {
                resultLog.push(count);
                break;
            } else {
                docList.shift();
            }
        } else {
            docList.push(docList.shift());
        }
    }
}
console.log(resultLog.join('\n'))