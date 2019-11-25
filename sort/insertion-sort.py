def insertionSort(seq):
    print("Insertion Sort Start...")
    if isinstance(seq, list) is False or len(seq) < 2:
        return
    # start from the second element of the original sequnce
    for index in range(len(seq)):
        if index == 0:
            continue
        # from the last element of child sequnce,
        # till the first element of child sequnce,
        # if the element is greater than the previous element,
        # exchange them,
        # if not,
        # stop traverse
        for idx in range(index, -1, -1):
            if(idx == 0):
                break
            if seq[idx] < seq[idx - 1]:
                tmp = seq[idx]
                seq[idx] = seq[idx - 1]
                seq[idx - 1] = tmp
                continue
            break
        print("round: " + str(index) + ": " + str(seq))


if __name__ == '__main__':
    seq = [5, 2, 4, 6, 1, 3]
    print("original seq: ", seq)
    insertionSort(seq)
