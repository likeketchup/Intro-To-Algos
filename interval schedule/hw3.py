# -*- coding: utf-8 -*-
"""
toma 9/27/2021 life is good today
"""
from typing import List 

def finish_first(intervals:List[List[int]])->int:
    count:int = 0
    end:int = 0
    while(intervals):
        i = intervals.pop(0)
        if(i[0]<end):
            continue
        end = i[1]
        count+=1
    return count

def parse_input(num_jobs:int)-> List[List[int]]:
    list_of_intervals : List = []
    for _ in range(num_jobs):
        i:List =list(map(int,input().split()))
        list_of_intervals.append(i)
    list_of_intervals = sorted(list_of_intervals,key = lambda l:l[1])
    return list_of_intervals

if __name__ =="__main__":
    num_instances=int(input())
    for _ in range(num_instances):
        num_jobs : int = int(input())
        print(finish_first(parse_input(num_jobs)))