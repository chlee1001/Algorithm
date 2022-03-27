/**
 * 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
 * 각 물건은 무게(w)와 가치(v)로 표현될 수 있음
 * 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음, 그래서 Fractional Knapsack Problem 으로 부름
 * Fractional Knapsack Problem 의 반대로 물건을 쪼개서 넣을 수 없는 배낭 문제도 존재함 (0/1 Knapsack Problem 으로 부름)
 */

const dataList = [[10, 10], [15, 12], [20, 10], [25, 8], [30, 5]]

function getMaxValue (dataList, capacity) {
  dataList.sort((a, b) => b[1] / b[0] - a[1] / a[0]) // 무게대비 가치가 높은 것 순으로 정렬
  let totalValue = 0
  const valueDetails = []

  for (const data of dataList) {
    if (capacity - data[0] >= 0) {
      totalValue += data[0]
      capacity -= data[0]
      valueDetails.push([data[0], data[1], 1])
    } else {
      const fraction = capacity / data[0]
      totalValue += data[1] * fraction
      capacity -= data[0] * fraction
      valueDetails.push([data[0], data[1], fraction])
      break
    }
  }

  console.log(valueDetails)
  return totalValue

}

console.log(getMaxValue(dataList, 30))