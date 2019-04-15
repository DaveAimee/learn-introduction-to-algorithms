

def find_maximum_sub_array_linear(array, low, high):
    n = high - low + 1
    max_sum = float('-inf')
    ending_sum = float('-inf')
    for j in range(0, n):
        ending_high = j
        if ending_sum < 0:
            ending_low = ending_high
            ending_sum = array[ending_high]
        else:
            ending_sum = ending_sum + array[j]
        if ending_sum > max_sum:
            max_sum = ending_sum
            max_low = ending_low
            max_high = ending_high
    return max_low, max_high, max_sum


if __name__ == '__main__':
    test = [-3, 7, 15, -2, 8, -9]
    r = find_maximum_sub_array_linear(test, 0, len(test) - 1)
    print(r)
    print(more_clear_sub_array_linear(test))

