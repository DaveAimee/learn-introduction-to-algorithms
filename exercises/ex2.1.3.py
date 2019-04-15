def find(list_a, v):
    for i, e in enumerate(list_a):
        if list_a[i] == v:
            return i
    return None


if __name__ == "__main__":
    test_list = [1,5,9,7,6]
    test_v = 8
    print(find(test_list, test_v))

