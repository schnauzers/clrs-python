# heap sort


# Utility Function to get parent node by index
# i is the index of array member
def getParent(i):
    idx = (i-1)//2
    if idx >= 0:
        return idx
    else:
        return None


# Utility Function to get left child node by index
def getLeftChild(i, arr):
    idx = 2*i + 1
    if idx < len(arr):
        return idx
    else:
        return None


# Utility Function to get right child node by index
def getRightChild(i, arr):
    idx = 2*i + 2
    if idx < len(arr):
        return idx
    else:
        return None


# Given an array A and an index i
# assume left tree of i and right tree of i are max heaps
# make tree with root i to be a max heap
# heapsize is used to control how much elements to be processed
def maxHeapify(A, i, heapsize):
    largest = i
    leftIdx = getLeftChild(i, A)
    if leftIdx is not None and leftIdx < heapsize and A[leftIdx] > A[i]:
        largest = leftIdx

    rightIdx = getRightChild(i, A)
    if rightIdx is not None and rightIdx < heapsize and \
            A[rightIdx] > A[largest]:
        largest = rightIdx
    # notice that the process need to be continued
    # only if larest is not i
    # otherwise, the process stops
    if largest is not i:
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp
        maxHeapify(A, largest, heapsize)


# for every node which is not leaf node
# adjust it to a max heap
def buildMaxHeap(A):
    for i in range(len(A)//2, -1, -1):
        maxHeapify(A, i, len(A))


# final function for heapsort
def heapSort(A):
    # firstly, reconstruct A to be a max heap
    buildMaxHeap(A)
    heapsize = len(A)

    # find max element for every step
    for i in range(len(A) - 1, 0, -1):
        tmp = A[0]
        A[0] = A[i]
        A[i] = tmp
        heapsize = heapsize - 1
        maxHeapify(A, 0, heapsize)


if __name__ == '__main__':
    print("--->Test utility functions...")
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("original A is: ", str(A))
    for idx, val in enumerate(A):
        print("<-------index: % d, value:: %d------->" % (idx, val))
        parentIdx = getParent(idx)
        if parentIdx is not None:
            print("parent node of %d: %d" % (A[idx], A[parentIdx]))
        else:
            print("This is Root Node")

        leftChildIdx = getLeftChild(idx, A)
        if leftChildIdx is not None:
            print("left node of %d: %d" % (A[idx], A[leftChildIdx]))
        else:
            print('\n')
            continue

        rightChildIdx = getRightChild(idx, A)
        if rightChildIdx is not None:
            print("right node of %d: %d" % (A[idx], A[rightChildIdx]))
        print('\n')

    print("--->Test maxHeapify...")
    A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print("original A is: ", str(A))
    print("lfet and right tree of index 1 are both max heap befor process")
    maxHeapify(A, 1, len(A))
    print("after call maxHeapify to process index 1:")
    print(A)
    print('\n')

    print("--->Test buildMaxHeap...")
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("original A is: ", str(A))
    buildMaxHeap(A)
    print("processed A is: ", str(A))
    print('\n')

    print("--->Test heapSort...")
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("original A: ", str(A))
    heapSort(A)
    print("sorted A: ", str(A))
