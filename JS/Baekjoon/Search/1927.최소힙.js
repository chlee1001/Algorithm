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

  /**
   * 최근 삽입한 노드가 제 자리를 찾아갈 수 있도록 맨 아래에서 위로 올리는 함수
   */
  heapifyUp = () => {
    let index = this.heap.length - 1
    const lastInsertedNode = this.heap[index]

    while (index > 0) {
      const parentIndex = this.getParentIndex(index)

      // 부모 노드의 값이 마지막에 삽입된 노드의 값 보다 크면
      // 부모 노드의 위치를 아래로 나린다
      if (this.heap[parentIndex] > lastInsertedNode) {
        this.heap[index] = this.heap[parentIndex]
        index = parentIndex
      } else {
        break
      }
    }

    // 부모 노드가 자리 잡았을 때 index에
    // 가장 나중에 삽입된 노드를 넣어준다.
    this.heap[index] = lastInsertedNode
  }

  /**
   * 최근 최상위 부모로 바뀐 노드를 올바른 위치로 내려주기 위한 함수
   */
  heapifyDown = () => {
    let index = 0
    const count = this.heap.length
    const rootNode = this.heap[index]

    while (this.getLeftChildIndex(index) < count) {
      const leftChildIndex = this.getLeftChildIndex(index)
      const rightChildIndex = this.getRightChildIndex(index)

      // 왼쪽 오른쪽 자식노드 중 더 작은 노드를 찾는다.
      // rightChild가 존재하면 더 작은 값을 찾는다.
      // 없으면 leftChild가 더 작은 값을 가지는 인덱스가 된다
      const smallerChildIndex =
        rightChildIndex && this.heap[rightChildIndex] <
        this.heap[leftChildIndex]
          ? rightChildIndex
          : leftChildIndex

      // 자식 노드의 값이 부모노드보다 작으면 위로 올린다.
      if (this.heap[smallerChildIndex] <= rootNode) {
        this.heap[index] = this.heap[smallerChildIndex]
        index = smallerChildIndex
      } else {
        break
      }

      // 비교 대상의 노드 위치에는 루드노드가 들어간다.
      this.heap[index] = rootNode
    }
  }

  /**
   * 힘 데이터 추가
   * @param key
   * 1. 맨 마지막에 새로운 데이터 추가
   * 2. 부모 노드의 값을 비교하여 부모가 더 크면 부모 노드와 자식 노드의 위치 교환 (HeapifyUp)
   * 3. 2번 반복
   */
  insert = (key) => {
    this.heap.push(key)
    this.heapifyUp()
  }

  /**
   * 힙 데이터 삭제
   * 1. 루트노드 삭제
   * 2. 맨 마지막 노드를 루트 노드위치로 올린다
   * 3. 양쪽 자식 노드와 값을 비교하여 더 작은 자식 노드와 위치를 변경한다.
   * 4. 3번 반복 // 자식노드가 없거나, 부모노드가 자식노드보다 작을 경우까지 반복
   */
  remove = () => {
    const count = this.heap.length
    const rootNode = this.heap[0]

    if (count <= 0) return undefined
    if (count === 1) {
      this.heap = []
    } else {
      this.heap[0] = this.heap.pop() // 맨 마지막 노드를 부모로 올린다
      this.heapifyDown() // 다시 min heap 형태를 갖추기
    }
    return rootNode
  }
}

const heap = new Heap()
const result = []

input.forEach(inputNum => {
  const num = Number(inputNum)

  if (num === 0) {
    const value = heap.remove()
    result.push(value === undefined ? 0 : value)
  } else {
    heap.insert(num)
  }
})
console.log(result.join('\n'))