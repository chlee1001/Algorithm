const [N, ...input] = require('fs').
  readFileSync('/dev/stdin').
  toString().
  trim().
  split('\n')

const executeTime = input[0].split(' ').sort((a, b) => a - b)

let waitingTime = 0
let totalTime = 0

function getTotalTime (executeTime) {
  executeTime.map((time) => {
    waitingTime += Number(time)
    totalTime += waitingTime
  })

  return totalTime
}
console.log(getTotalTime(executeTime))