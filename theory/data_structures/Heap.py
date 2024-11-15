class MyMinHeap:
    def __init__(self, heap):
        self._heap = heap

    def push(self, value):
        self._heap.append(value)
        _helper_percolate_up(self._heap, len(self._heap)-1)

    def pop(self):
        value = self._heap[0]
        _helper_swap(self._heap, 0, -1)
        self._heap.pop(-1)
        _helper_percolate_down(self._heap, len(self._heap), 0)
        return value

def _helper_swap(array, first, second):
    temp = array[second]
    array[second] = array[first]
    array[first] = temp

def _helper_percolate_down(heap, n, i):
    # hasAnyChild        = (2*i) < n
    # hasRightChild      = (2*i+1) < n
    # isRightSmallest    = heap[2*i+0] > heap[2*i+1]
    # isGreaterThanLeft  = heap[i] > heap[2*i+0]
    # isGreaterThanRight = heap[i] > heap[2*i+1]
    while (2*i) < n:
        if ((2*i+1) < n) and (heap[2*i+0] > heap[2*i+1]) and (heap[i] > heap[2*i+1]):
            _helper_swap(heap, i, 2*i+1)
            i = 2*i+1
        elif (heap[i] > heap[2*i+0]):
            _helper_swap(heap, i, 2*i+0)
            i = 2*i+0
        else:
            break

def _helper_percolate_up(heap, i):
    # isLessThanParent = heap[i] > heap[2*i+1]
    while i > 0:
        if heap[i//2] > heap[i]:
            _helper_swap(heap, i//2, i)
            i = i//2
        else:
            break

def heapify(array):
    heap = [a for a in array]
    n = len(heap)
    cur = (n-1)//2
    
    for index in range(cur, -1, -1):
        _helper_percolate_down(heap, n, index)
        
    return heap

if __name__ == '__main__':
    testCases = [
        {
            'case': [9, 15, 5, 7, 12, 17, 3],
            'expectation': [3, 5, 9, 7, 12, 17, 15]
        },
        {
            'case': [20, 1, 30, 40, 10, 5],
            'expectation': [1, 5, 10, 40, 20, 30]
        },
        {
            'case': [4, 8, 6, 3, 7, 9, 2, 5],
            'expectation': [2, 3, 6, 4, 7, 9, 8, 5]
        }
    ]
    
    for i in range(len(testCases)):
        print('--------------------------------------')
        case = testCases[i]['case']
        expectation = testCases[i]['expectation']
        actual = heapify(case)
        print(case)
        print(actual, '==', expectation)
        assert (actual == expectation)
        myheap = MyMinHeap(actual)
        v = myheap.pop()
        print(v, '<-', actual)
        a = 11
        myheap.push(a)
        print(a, '->', actual)
