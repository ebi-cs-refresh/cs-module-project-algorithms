import collections
import sys
INT_MIN = -sys.maxsize - 1
INT_MAX = sys.maxsize
print(INT_MIN)
print("INT_MAX", INT_MAX)
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):  # this is fixed windows

    maxVal = 0
    currentSum = 0
    res = []
    combo = []
    bigger = []

    # grow the initial length
    for i in range(len(nums)):
        # add val to current running sum
        currentSum += nums[i]
        combo.append(nums[i])

        # is the sum greater than (or equal to) val k-1

        if i >= k-1:  # i -> how far we are in the arr
            # print("combo", combo)
            maxVal = max(maxVal, currentSum)
            res.append(maxVal)
            # move to the next subset
            currentSum -= nums[i-(k-1)]
            print("combo2", combo)
            bigger.append(max(combo))
    return bigger


def sliding_window_max2(nums, k):  # this is fixed windows

    maxVal = 0
    currentSum = 0

    # grow the initial length
    for i in range(len(nums)):
        # add val to current running sum
        currentSum += nums[i]
        # is the sum greater than (or equal to) val k-1

        if i >= k-1:  # i -> how far we are in the arr
            maxVal = max(maxVal, currentSum)
            # move to the next subset
            currentSum -= nums[i-(k-1)]

    return maxVal


def sliding_window_min(k, nums):  # this is fixed windows
    if nums == None or len(nums) == 0:
        return 0
    if len(nums) <= 2:
        if sum(nums) >= s:
            return len(nums)
        else:
            return 0

    ans = INT_MAX
    left = 0  # left => start
    currentSum = 0

    # grow the initial length
    for i in range(len(nums)):
        # add val to current running sum

        currentSum += nums[i]

        while currentSum >= s:
            ans = min(ans, i-left+1)  # i+1-left --> current size of subarray
            currentSum -= nums[left]
            left += 1

    if ans == None:
        return 0
    else:
        return ans


def sliding_window_smallest_subarray(targetSum, nums):  # find the best k
    size = INT_MAX
    windowsum = 0
    start = 0

    for windend in range(len(nums)):
        # print(windend)
        # print("windowsum", windowsum)
        windowsum += nums[windend]

        # add values in linear fashion
        # if we exceed the value(greater than equal to target sum)

        # can i do better
        while windowsum >= targetSum:  # we're trying to shrink the target sum
            # windend-start+1 --> delta of when it starts
            size = min(size, windend-start+1)
            # shrink left hand size
            windowsum -= nums[start]
            start += 1
    return size


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    arr2 = [4, 2, 2, 7, 8, 1, 2, 8, 10]
    arr3 = [1, 3, -1, -3, 5, 3, 6, 7]
    arr_ = [2, 3, 1, 2, 4, 3]
    k = 3
    targetSum = 8
    s = 7

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr3, k)}")

    print(
        f"Output of sliding_window_max function is: {sliding_window_max2(arr, k)}")

    print(
        f"Output of sliding_window min function is: {sliding_window_min(s, arr_)}")

    # print(
    # f"Output of sliding_window_max function is: {maxSum(arr, k)}")

    print(
        f"Output of sliding_window_max function is: {sliding_window_smallest_subarray(targetSum, arr2)}")
