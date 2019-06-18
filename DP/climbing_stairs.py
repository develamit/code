#!/opt/local/bin/python
"""
42. Climbing Stairs
Code it now: https://oj.leetcode.com/problems/climbing-stairs/ Difficulty: Easy, Frequency: High
Question:
    You are climbing a staircase. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
import time

class climbing_stairs:
    def __init__(self, n, METHOD='MEMOIZATION'):
        print('Solving the climbing stairs DP problem for n = {} stairs using {} method'.format(n, METHOD))
        self.cache = [0]*(n + 1)
        #print('    Initial cache state = {}'.format(self.cache))

    def get_distinct_ways_simple_recursion(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        # simple recursion
        return(self.get_distinct_ways_simple_recursion(n - 1) + self.get_distinct_ways_simple_recursion(n - 2))



    def get_distinct_ways_memoization(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        # using memoization
        if self.cache[n] != 0:
            return self.cache[n]

        # recursive call when 1 step is taken + recursive call when 2 steps are taken in one shot
        #incorrect: return((1 + self.get_distinct_ways_memoization(n - 1)) + (1 + self.get_distinct_ways_memoization(n - 2)))
        #incorrect: return(1 + (self.get_distinct_ways_memoization(n - 1) + self.get_distinct_ways_memoization(n - 2)))

        # memoization technique - filling up a cache and preventing the same calls
        self.cache[n] = self.get_distinct_ways_memoization(n - 1) + self.get_distinct_ways_memoization(n - 2)
        return self.cache[n]



    # O(1) space using 2 variables and O(n) time
    # with cache the space will be more O(n)
    def get_distinct_ways_tabular(self, n):
        n1 = 1
        n2 = 2

        if n < 2:
            ##self.cache[1] = 1
            n2 = n1
        #else:
            ##self.cache[1] = 1
            ##self.cache[2] = 2

        # iterative - bottom - up approach
        for i in range(3, n + 1):
            #self.cache[i] = self.cache[i - 1] + self.cache[i - 2]
            tmp = n1 + n2
            n1 = n2
            n2 = tmp

        #return self.cache[n]
        return n2



if __name__ == '__main__':
    #stairsArr = [1, 2, 3, 4, 5, 6, 35]
    #METHOD = 'RECURSION'

    #stairsArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]
    #METHOD = 'MEMOIZATION'

    stairsArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5000]
    METHOD = 'TABULAR'

    if METHOD == 'RECURSION':
        for n in stairsArr:
            cs = climbing_stairs(n, METHOD)
            b = time.time()
            v = cs.get_distinct_ways_simple_recursion(n)
            e = time.time() - b
            print('    Distinct ways to climb {} stairs = {}. Time taken = {} seconds'.format(n, v, e))
            #print('    Final cache state = {}\n'.format(cs.cache))

    elif METHOD == 'MEMOIZATION':
        for n in stairsArr:
            cs = climbing_stairs(n, METHOD)
            b = time.time()
            v = cs.get_distinct_ways_memoization(n)
            e = time.time() - b
            print('    Distinct ways to climb {} stairs = {}. Time taken = {} seconds'.format(n, v, e))
            #print('    Final cache state = {}\n'.format(cs.cache))

    elif METHOD == 'TABULAR':
        for n in stairsArr:
            cs = climbing_stairs(n, METHOD)
            b = time.time()
            v = cs.get_distinct_ways_tabular(n)
            e = time.time() - b
            print('    Distinct ways to climb {} stairs = {}. Time taken = {} seconds'.format(n, v, e))
            #print('    Final cache state = {}\n'.format(cs.cache))
