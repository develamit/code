#!/usr/bin/python
"""
43. Unique Paths
Code it now: https://oj.leetcode.com/problems/unique-paths/ Difficulty: Medium, Frequency: Low
Question:
    A robot is located at the top-left corner of a m x n grid (marked Start in the diagram below). The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked Finish in the diagram below). How many possible unique paths are there?
"""

from array import *

class unique_paths:
    def __init__(self, m, n):
        self.rows = m
        self.cols = n
        #self.cache = [ [0] * (n + 1)] * (m + 1) # this creates shallow lists
        self.cache = [[0 for i in range(n + 1)] for j in range(m + 1)] 
        print('grid dimension: {} x {}'.format(m, n))
        print('initial cache...')
        for row in self.cache:
            print('{}'.format(row))


    def get_unique_paths_recursion(self, m, n):
        # base case
        if m == 1 and n == 1:
            return 0

        if m == 1:
            return 1
        elif n == 1:
            return 1
        #elif m == 2 and n == 2:
            #return 2

        v = self.get_unique_paths_recursion( (m - 1), n) + self.get_unique_paths_recursion( m, (n - 1))
        #print('grid val = {}'.format(self.cache[m][n]))

        return v




    def get_unique_paths_memoization(self, m, n):
        # base case
        if m == 1 and n == 1:
            return 0

        if m == 1:
            self.cache[m][n] = 1
            return 1
        elif n == 1:
            self.cache[m][n] = 1
            return 1

        if self.cache[m][n] != 0:
            return self.cache[m][n]

        self.cache[m][n] = self.get_unique_paths_memoization( (m - 1), n) + self.get_unique_paths_memoization( m, (n - 1))
        return self.cache[m][n]


    #'''
    def get_unique_paths_tabular(self, m, n):
        # base case
        if m == 1 and n == 1:
            return 0

        if m == 1:
            self.cache[m][n] = 1
            return 1
        elif n == 1:
            self.cache[m][n] = 1
            return 1

        else:
            self.cache[1][1] = 0
            self.cache[1][2] = 1
            self.cache[2][1] = 1

        for i in range(2, m):
            for j in range(2, n):
                self.cache[m][n] = self.cache[(m - 1)][n] + self.cache[m][(n - 1)]

        return self.cache[m][n]
    #'''


if __name__ == '__main__':
    m = 5
    n = 5

    #up = unique_paths(m, n)
    #num_paths = up.get_unique_paths_recursion(m, n)
    #print('    Grid: {} x {} has {} unique paths'.format(m, n, num_paths))

    up = unique_paths(m, n)
    num_paths = up.get_unique_paths_memoization(m, n)
    print('    Grid: {} x {} has {} unique paths (memoization)'.format(m, n, num_paths))
    print('final cache...')
    for row in up.cache:
        print('{}'.format(row))
    print('\n')

    up = unique_paths(m, n)
    num_paths = up.get_unique_paths_tabular(m, n)
    print('    Grid: {} x {} has {} unique paths (tabular)'.format(m, n, num_paths))
    print('final cache...')
    for row in up.cache:
        print('{}'.format(row))
    print('\n')

