"""
Write a function that returns True if one array is a rotation of another
"""

#==================================
# Approach 1: O(n) time O(1) space
#           Other possible approaches would be
#           1. Sort the arrays - O(nlogn)
#           2. Use a hash/dict - O(n) space
#==================================
# Implement your function below.
def is_rotation(list1, list2):
    
    idx1 = 0 # ptr for list1
    idx2 = 0 # ptr for list2
    
    # if the lists do not have the same number of elements then it cannot be a rotation
    # of each other
    if len(list1) != len(list2):
        return False
    
    # find the starting point in list1, which matches with list2
    while list1[idx1] != list2[idx2]:
        idx1 += 1
       
    # now keep traversing list2 and keep comparing 
    while idx2 < len(list2):
        if idx1 >= len(list1):
            idx1 = 0
            
        if list1[idx1] != list2[idx2]:
            return False
            
        idx2 += 1
        idx1 += 1
    
    
    return True

if __name__ == '__main__':
    # NOTE: The following input values will be used for testing your solution.
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2a = [4, 5, 6, 7, 8, 1, 2, 3]
    ret = is_rotation(list1, list2a)
    print('list: {}, list2: {} rotation = {}'.format(list1, list2a, ret))
    # is_rotation(list1, list2a) should return False.

    list2b = [4, 5, 6, 7, 1, 2, 3]
    ret = is_rotation(list1, list2b)
    print('list: {}, list2: {} rotation = {}'.format(list1, list2b, ret))
    # is_rotation(list1, list2b) should return True.

    list2c = [4, 5, 6, 9, 1, 2, 3]
    ret = is_rotation(list1, list2c)
    print('list: {}, list2: {} rotation = {}'.format(list1, list2c, ret))
    # is_rotation(list1, list2c) should return False.

    list2d = [4, 6, 5, 7, 1, 2, 3]
    ret = is_rotation(list1, list2d)
    print('list: {}, list2: {} rotation = {}'.format(list1, list2d, ret))
    # is_rotation(list1, list2d) should return False.

    list2e = [4, 5, 6, 7, 0, 2, 3]
    ret = is_rotation(list1, list2e)
    print('list: {}, list2: {} rotation = {}'.format(list1, list2e, ret))
    # is_rotation(list1, list2e) should return False.

    list2f = [1, 2, 3, 4, 5, 6, 7]
    ret = is_rotation(list1, list2f)
    print('list: {}, list2: {} rotation = {}'.format(list1, list2f, ret))
    # is_rotation(list1, list2f) should return True.

    list2g = [7, 1, 2, 3, 4, 5, 6]
    ret = is_rotation(list1, list2g)
    print('list: {}, list2: {} rotation = {}'.format(list1, list2g, ret))
    # is_rotation(list1, list2g) should return True.

