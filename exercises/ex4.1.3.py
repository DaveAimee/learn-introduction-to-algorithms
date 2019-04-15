import time
import random
def find_max_cross_sub_array(array, low, mid, high):
    left_sum = float('-inf')
    sum_ = 0
    for i in range(mid, low-1, -1):
        sum_ = sum_ + array[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i
    right_sum = float('-inf')
    sum_ = 0
    for j in range(mid+1, high+1, 1):
        sum_ = sum_ + array[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j
    return max_left, max_right, right_sum + left_sum


def find_max_sub_array(array, low, high):
    if low == high:
        return low, high, array[low]  # base case, only one element
    else:
        mid = (low + high)//2  # downward rounding to integer
        (left_low, left_high, left_sum) = find_max_sub_array(array, low, mid)
        (right_low, right_high, right_sum) = find_max_sub_array(array, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_cross_sub_array(array, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_sub_array_brute_force(array, low, high):
    max_sum = float('-inf')
    for i in range(low, high + 1, 1):
        sum_ = 0
        for j in range(i, high + 1, 1):
            sum_ = sum_ + array[j]
            if sum_ > max_sum:
                max_sum = sum_
                max_i = i
                max_j = j
    return max_i, max_j, max_sum


if __name__ == '__main__':
    test = [-3, 7, 15, -2, 8, -9]
    for n in range(1, 1001):
        test_array = random.sample(range(1, 20000), n)
        start_stamp = time.time()
        result_recursive = find_max_sub_array(test_array, 0, len(test_array) - 1)
        recursive_stamp = time.time()
        result_brute = find_max_sub_array_brute_force(test_array, 0, len(test_array) - 1)
        brute_stamp = time.time()
        if brute_stamp - recursive_stamp < recursive_stamp - start_stamp:
            break
    print(n)
    r = find_max_sub_array(test, 0, len(test) - 1)
    print(r)





