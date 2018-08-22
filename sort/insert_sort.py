# 插入排序
"""
   Topic: sample code in book
   Desc: 插入排序
         由于其内层循环非常紧凑，对于小规模的输入，插入排序是一种非常快的原址排序方法。
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Yang Liu"


def insert_sort(seq):
    for j in range(1, len(seq)):
        key = seq[j]
        # insert arras[j] into the sorted
        i = j-1
        while i >= 0 and seq[i] > key:
            seq[i+1] = seq[i]
            i -= 1
        seq[i+1] = key


if __name__ == '__main__':
    seq = [5, 2, 4, 6, 1, 3]
    insert_sort(seq)
    print(seq)

