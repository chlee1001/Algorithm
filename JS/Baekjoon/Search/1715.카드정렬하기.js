const [N, ...input] = require('fs').
  readFileSync('/dev/stdin').
  toString().
  trim().
  split('\n')

class Heap {
  constructor () {
    this.heap = []
  }

  getLeftChildIndex = parentIndex => parentIndex * 2 + 1
  getRightChildIndex = parentIndex => parentIndex * 2 + 2
  getParentIndex = childIndex => Math.floor((childIndex - 1) / 2)

  heapifyUp = () => {
    let index = this.heap.length - 1
    const lastInsertedNode = this.heap[index]

    while (index > 0) {
      const parentIndex = this.getParentIndex(index)

      if (this.heap[parentIndex] > lastInsertedNode) {
        this.heap[index] = this.heap[parentIndex]
        index = parentIndex
      } else {
        break
      }
    }

    this.heap[index] = lastInsertedNode
  }

  heapifyDown = () => {
    let index = 0
    const count = this.heap.length
    const rootNode = this.heap[index]

    while (this.getLeftChildIndex(index) < count) {
      const leftChildIndex = this.getLeftChildIndex(index)
      const rightChildIndex = this.getRightChildIndex(index)

      const smallerChildIndex =
        rightChildIndex && this.heap[rightChildIndex] <
        this.heap[leftChildIndex]
          ? rightChildIndex
          : leftChildIndex

      if (this.heap[smallerChildIndex] <= rootNode) {
        this.heap[index] = this.heap[smallerChildIndex]
        index = smallerChildIndex
      } else {
        break
      }

      this.heap[index] = rootNode
    }
  }

  insert = (key) => {
    this.heap.push(key)
    this.heapifyUp()
  }

  remove = () => {
    const count = this.heap.length
    const rootNode = this.heap[0]

    if (count <= 0) return undefined
    if (count === 1) {
      this.heap = []
    } else {
      this.heap[0] = this.heap.pop()
      this.heapifyDown()
    }
    return rootNode
  }
}

let result = 0
const heap = new Heap()

input.forEach(value => {
  heap.insert(Number(value))
})

while (heap.heap.length - 1 > 0) {
  const num1 = heap.remove()
  const num2 = heap.remove()
  heap.insert(num1 + num2)
  result += num1 + num2
}
console.log(result)
