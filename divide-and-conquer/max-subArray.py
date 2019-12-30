# find MaxSubArray of subArray where mid element sits in
def findMaxCrossingSubArray(A, low, mid, high):
    maxLeft = 0
    leftSum = float('-inf')
    sum = 0
    for i in range(mid, -1, -1):
        sum = sum + A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i

    maxRight = 0
    rightSum = float('-inf')
    sum = 0
    for i in range(mid+1, high + 1, 1):
        sum = sum + A[i]
        if sum > rightSum:
            rightSum = sum
            maxRight = i

    return (maxLeft, maxRight, leftSum + rightSum)


# recursive method to find maxSubArray
def findMaxSubArray(A, low, high):
    print("low: ", low, "high: ", high)
    # recursive stop contidion
    if low == high:
        return(low, high, A[low])
    else:
        mid = (low + high)//2
        # subArray sits in left subarray
        # or right subarray
        # or cross them
        # find maxium of them as the final result
        leftLow, leftHigh, leftSum = findMaxSubArray(A, low, mid)
        righLow, righHigh, rightSum = findMaxSubArray(A, mid + 1, high)
        crossLow, crossHigh, crossSum = findMaxCrossingSubArray(
            A, low, mid, high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return(leftLow, leftHigh, leftSum)
        elif rightSum >= leftSum and rightSum >= crossSum:
            return(righLow, righHigh, rightSum)
        else:
            return(crossLow, crossHigh, crossSum)


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    maxSubArray = findMaxSubArray(A, 0, len(A) - 1)
    print("maxSubArrayLeftIndex: ", maxSubArray[0])
    print("maxSubArrayRightIndex: ", maxSubArray[1])
    print("maxSubArraySum: ", maxSubArray[2])
