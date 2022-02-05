const [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const resultLog = [];

for (let i = 0; i < N * 2; i += 2) {
    let [N, M] = input[i].split(" ").map(num => parseInt(num, 10));
    const docList = input[i + 1].split(" ").map(num => parseInt(num, 10));
    // const priorityList = Array.from(docList).sort((a, b) => a - b);
    // const targetDoc = docList[M];
    let  count = 0;

    while (docList.length !== 0) {
        let maxValue = Math.max(...docList);
        let front = docList.shift();
        M -= 1;

        if (maxValue === front) {
            count += 1;
            if (M < 0) {
                resultLog.push(count);
                break;
            }
        } else {
            docList.push(front);
            if (M < 0) {
                M = docList.length - 1;
            }
        }
    }
}

console.log(resultLog.join("\n"));