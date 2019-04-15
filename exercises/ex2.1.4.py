def add_binary(list_a, list_b):
    list_c = []
    carry = 0
    for i in range(len(list_a), 0, -1):
        temp = list_a[i-1]+list_b[i-1]+carry
        if temp > 1:
            list_c.insert(0, temp % 2)
            carry = 1
        else:
            list_c.insert(0, temp)
            carry = 0
    list_c.insert(0, carry)
    return list_c


if __name__ == "__main__":
    A = [1, 0, 1, 1]
    B = [1, 1, 1, 0]
    print(add_binary(A, B))