const [N] = require('fs').
  readFileSync('/dev/stdin').
  toString().
  trim().
  split('\n')

const coinList = [500, 100, 50, 10, 5, 1]

function getCoinCount (value) {
  let totalCoinCount = 0
  let change = 1000 - value

  coinList.map(coin => {
    const coinNum = Math.floor(change / coin)
    change -= coinNum * coin
    totalCoinCount += coinNum
  })
  return totalCoinCount
}

console.log(getCoinCount(N))