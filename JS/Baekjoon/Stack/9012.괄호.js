const [T, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let resultLog = '';


input.map(data => {
    const testSet = data.split('');
    let resultStatus = 0;

    for (let i = 0; i < testSet.length; i++) {
        const bracket = testSet[i];

        if (bracket === '(') {
            resultStatus += 1;
        } else if (bracket === ')') {
            resultStatus -= 1;
        }
        if (resultStatus < 0) {
            resultLog += 'NO\n';
            break
        }
    }

    if (resultStatus === 0) {
        resultLog += 'YES\n';
    } else if (resultStatus > 0) {
        resultLog += 'NO\n';
    }
})


console.log(resultLog)