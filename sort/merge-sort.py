# assume that A is an array
# the goal is to sort an child sequnce of A(by ascending order)
# p is the start element index of the child sequnce
# r is the last element index of the child sequnce
# elements [p, q] is a sorted child sequence
# elements [q+1, r] is also a sorted child sequence


def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    # append positive infinity as facility to aviod
    # L or R is out of elements during traversing
    # just for clean code
    L.append(float("inf"))
    R.append(float("inf"))
    print("L: ", L)
    print("R: ", R)

    idxL = 0
    idxR = 0
    for idxA in range(p, r+1):
        print("idxL: ", idxL, " idxR: ", idxR)
        if L[idxL] <= R[idxR]:
            A[idxA] = L[idxL]
            idxL = idxL + 1
        else:
            A[idxA] = R[idxR]
            idxR = idxR + 1
        print("round ", idxA, "of sorting result: ", A)


def mergeSort(A, p, r):
    if p < r:
        q = (p + r)//2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)


if __name__ == '__main__':
    A = [2, 4, 5, 7, 1, 2, 3, 6]
    print("original seq: ", A)
    # merge(A, 0, 3, 7)
    B = [1, 3, 7, 2, 4, 9, 10, 1, 11, 12, 18, 9]
    mergeSort(B, 0, len(B)-1)
