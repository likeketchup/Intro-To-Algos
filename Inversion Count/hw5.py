# -*- coding: utf-8 -*-
"""
toma 10/13/2021 time flies, three OA due Friday, confused
"""
from typing import List,Tuple

def merge_sort(input:List[int])->Tuple[List[int],int]:
    if len(input)==1:
        return input,0
    midpoint = len(input)//2
    sortedLeft,count1=merge_sort(input[:midpoint])
    sortedRight,count2=merge_sort(input[midpoint:])
    sorted, count3 = merge_and_count(sortedLeft[::-1],sortedRight[::-1])
    return sorted, count3+count2+count1
    
def merge_and_count(L,R):
#cat test.txt | python3 hw5.py
    #i,j = 0,0
    count = 0
    sorted = []
    while L or R:
        # if L list is empty
        if not L:
            sorted.append(R.pop())
            continue
        elif not R:
            sorted.append(L.pop())
            continue
        if(L[-1]>R[-1]):
            sorted.append(R.pop())
            count+=len(L)
        else:
            sorted.append(L.pop())
    return sorted, count


if __name__ =="__main__":
    num_instances=int(input())
    for _ in range(num_instances):
        num_elements : int = int(input())
        nums = input().split()
        nums = list(map(int ,nums))
        _, count = merge_sort(nums)
        print(count)