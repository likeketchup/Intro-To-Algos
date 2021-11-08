# -*- coding: utf-8 -*-
"""
toma 11/4 shakespeare midterm tomorrow
"""
from typing import List, Tuple


def knapsack(c: int, items: List[List[int]]) -> int:
    curr_c = 0
    bellman = [[0 for _ in range(c+1)] for _ in range(len(items)+1)]
    for i in range(0,len(items)):
        wi, vi = items[i]
        for j in range(c+1):
            # wi is j
            if(wi<=j):
                bellman[i+1][j] = max(bellman[i][j], bellman[i][j-wi]+vi)
            else:
                bellman[i+1][j] = bellman[i][j]
    return bellman[-1][-1]


if __name__ == "__main__":
    num_instances = int(input())
    for _ in range(num_instances):
        nums, capacity = input().split()
        items = []
        for i in range(int(nums)):
            temp = input().split()
            items.append([int(temp[0]), int(temp[1])])
        print(knapsack(int(capacity), items))