# -*- coding: utf-8 -*-
"""
toma 10/27 fucked up quizes
"""
from typing import List,Tuple
def int32(x):
  if x>0xFFFFFFFF:
    raise OverflowError
  if x>0x7FFFFFFF:
    x=int(0x100000000-x)
    if x<2147483648:
      return -x
    else:
      return -2147483648
  return x

def merge_sort(input:List[List[int]])->int:
    sorted_copy = sorted(input, key=lambda x: x[1])
    n = len(input)
    res = [None] * n
    res[0] = sorted_copy[0][2]
    for i in range(1,n):
        index = -1
        for j, x in enumerate(sorted_copy):
            if not j<i:
                break
            if x[1]<=sorted_copy[i][0]:
                index = j
        if index == -1:
            res[i] = res[i-1]
            continue
        res[i] = max(res[i-1],res[index]+ sorted_copy[i][2])
    return int32(res[-1])


if __name__ =="__main__":
    num_instances=int(input())
    for _ in range(num_instances):
        num_elements : int = int(input())
        list_of_lists = []
        for i in range(num_elements):
            nums = input().split()
            nums = list(map(int ,nums))
            list_of_lists.append(nums)
        print(merge_sort(list_of_lists))