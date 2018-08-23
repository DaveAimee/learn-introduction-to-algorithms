#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 快速排序
"""
    Topic: sample
    Desc: 快速排序
    采用分治法思想：
    分解： 将数组A[p..r]划分为两个（可能为空）子数组A[p..q-1]和A[q+1,r]，使得A[p..q-1]
    中的每一个元素都小于等于A[q],而A[q]也小于等于A[q+1..r]中的每个元素。
    解决：递归调用快速排序，对于数组A[p..q-1]和A[q+1..r]进行排序。
    合并：原址排序，不需要合并操作。
"""
from random import randint

def __quickSubSortTail(seq, p, r):
    """循环版本，模拟尾递归，可以大大减少递归栈深度，而且时间复杂度不变"""
    while p < r:
        q = __rand_partition(seq, p, r)
        if q - p < r - q:
            __quickSubSortTail(seq, p, q - 1)
            p = q + 1
        else:
            __quickSubSortTail(seq, q + 1, r)
            r = q - 1


def quick_sort(seq):
    # __quick_sub_sort(seq, 0, len(seq) - 1)
    __quickSubSortTail(seq, 0, len(seq) - 1)


def __quick_sub_sort(seq, p, r):
    "递归版本"
    if p < r:
        q = __rand_partition(seq, p, r)
        __quick_sub_sort(seq, p, q-1)
        __quick_sub_sort(seq, q+1, r)


def __partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def __rand_partition(A, p, r):
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return __partition(A, p, r)


if __name__ == "__main__":
    s = [9, 7, 8, 10, 16, 3, 14, 2, 1, 4]
    quick_sort(s)
    print(s)
