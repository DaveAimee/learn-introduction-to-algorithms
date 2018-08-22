#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 归并排序(分治法)
"""
    Topic: sample
    Desc : 归并排序
        归并排序算法完全遵循分治模式，操作如下：
        分解： 分解待排序的n个元素序列成各具n/2个元素的两个子序列
        解决： 使用归并排序递归的排序两个子序列
        合并： 合并两个已排序的子序列以产生已排序的答案
"""
__author__ = 'Yang Liu'
import math
def merge_sort(seq):
    merge_sort_range(seq,0,len(seq)-1)

def merge_sort_range(seq, start, end):
    if start < end:
        middle = math.floor((start+end)/2)
        merge_sort_range(seq, start, middle)
        merge_sort_range(seq, middle+1, end)
        merge(seq, start, middle, end)

def merge(seq, start, middle, end):
    """
    left <= middle <= right
    子数组seq[left..middle]和seq[middle+1..right]都是排好序的。
    将左右两边排好序的数组归并到原数组seq中。
    :param seq: 待排序序列
    :param start: 起始标号
    :param middle:中部标号
    :param end:尾部标号
    :return:无
    """
    tempSeq = []
    i = start
    j = middle+1
    while i <= middle and j <= end:
        if seq[i] <= seq[j]:
            tempSeq.append(seq[i])
            i += 1
        else:
            tempSeq.append(seq[j])
            j += 1
    if i <= middle:
        tempSeq.extend(seq[i:middle + 1])
    else:
        tempSeq.extend(seq[j:end + 1])
    seq[start:end+1] = tempSeq[:]


if __name__ == '__main__':
    aa = [4, 2, 5, 1, 6, 3, 7, 9, 8]
    merge_sort(aa)
    print(aa)


