const [N, ...input] = require('fs').
  readFileSync('/dev/stdin').
  toString().
  trim().
  split('\n')

const executeTime = input[0].split(' ').sort((a, b) => a - b)
const waitingTime = []

function getTotalTime (executeTime) {
  executeTime.map((time, idx) => {
    if (waitingTime.length > 0) {
      waitingTime.push(waitingTime[idx - 1] + Number(time))
      return
    }
    waitingTime.push(Number(time))
  })
  return waitingTime.reduce((a, b) => a + b)
}

console.log(getTotalTime(executeTime))