const [N, K, ...inputData] = require('fs').
  readFileSync('/dev/stdin').
  toString().
  trim().
  split('\n')

const sensors = inputData[0].split(' ').map(data => Number(data))
const perSensorsDistance = []
let minSum = 0

// 0. 집중국의 개수가 센서들의 개수보다 같거나 많으면 집중국의 수신가능 여역의 길이의 합은 0
if (Number(K) >= Number(N)) {
  console.log(0)
  return
}

// 1. 센서들의 좌표를 오름차순 정렬
sensors.sort((a, b) => a - b)

// 2. 각 센서 사이의 거리 계산
for (let i = 1; i <= sensors.length - 1; i++) {
  const distance = sensors[i] - sensors[i - 1]
  perSensorsDistance.push(distance)
}

// 3. 가장 거리가 먼 순서대로 k-1개의 연결고리 제거
perSensorsDistance.sort((a, b) => b - a)
for (let i = K - 1; i <= perSensorsDistance.length - 1; i++) {
  minSum += perSensorsDistance[i]
}

console.log(minSum)