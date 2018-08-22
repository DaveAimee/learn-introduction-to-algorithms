#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 堆排序
"""
   Topic: sample
   Desc: 堆排序
       堆排序的时间复杂度是O(nlg(n)),并且具有原址排序的特性。
       二叉堆heap是一种数据结构，可以用来实现优先队列。
       给定一个节点的下标i（下标从0开始），则其父节点、左子树、右子树为：
       parent(i)=floor((i+1)/2-1)=((i+1)>>1)-1
       left(i)=2*i+1=(i<<1)+1
       right(i)=2*i+2=(i+1)<<1
       最小堆定义：该节点的值小于所有子节点
       最大堆定义：该节点的值大于所有子节点
       在堆排序中使用最大堆。
       在优先队列算法中，使用最小堆。
"""
__author__ = "Yang Liu"


class Heap(object):
    def __init__(self, seq, heap_size, length):
        """
        :param seq:存放待排序的序列
        :param heap_size: 堆的大小
        :param length: 整个序列的大小
        """
        self.seq = seq
        self.heap_size = heap_size
        self.length = length


def heap_sort(seq):
    """
    堆排序算法。
    """
    heap = Heap(seq, len(seq), len(seq))
    __build_max_heap(heap)
    s = heap.seq
    for i in range(heap.length-1,-1,-1):
        s[0] , s[i] = s[i], s[0]
        heap.heap_size -= 1
        __max_heapify(heap, 0)


def __build_max_heap(heap):
    slen = heap.heap_size
    for i in range(((slen + 1) >> 1) - 1, -1, -1):
        __max_heapify(heap, i)


def __max_heapify(heap, i):
    """
    保持i节点处最大堆的性质。
    :param heap: Heap数据结构
    :param i: 节点序号
    :return:
    """
    seq = heap.seq
    slen = heap.heap_size
    while True:
        left = (i << 1) + 1
        right = (i + 1) << 1
        if left < slen and seq[left] > seq[i]: # 在i，left，right中找到largest标号
            largest = left
        else:
            largest = i
        if right < slen and seq[right] > seq[largest]:
            largest = right
        if largest != i:
            seq[largest], seq[i] = seq[i], seq[largest]
            i = largest
        else:
            break


if __name__ == '__main__':
    iSeq = [9, 7, 8, 10, 16, 3, 14, 2, 1, 4]
    heap_sort(iSeq)
    print(iSeq)

