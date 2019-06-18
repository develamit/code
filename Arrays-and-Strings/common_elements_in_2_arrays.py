"""
Find the common elements (return as an array) from 2 sorted ascending integer arrays
"""

#=================================================
# Approach 1
#=================================================
# Implement your function below.
def common_elements2(list1, list2):
    result = []

    n1 = len(list1)
    n2 = len(list2)

    idx1 = 0
    idx2 = 0

    # Find the longer list length
    n = n2
    if n1 > n2:
        n = n1

    # traverse the longer of the 2 lists
    for i in range(n):
        print('idx1: {},     idx2: {}'.format(idx1, idx2))
        if list1[idx1] == list2[idx2]:
            print('    matched idx1: {} elem1: {},     idx2: {} elem2: {}'.format(idx1,list1[idx1], idx2, list2[idx2]))
            result.append(list1[idx1])
            if idx1 < (len(list1) - 1):
                idx1 += 1
            if idx2 < (len(list2) - 1):
                idx2 += 1

        else:
            while (idx2 < len(list2) - 1) and (list1[idx1] > list2[idx2]):
                idx2 += 1
                continue

            while (idx1 < len(list1) - 1) and (list2[idx2] > list1[idx1]):
                idx1 += 1

    return result





#=================================================
# Approach 2 - cumbersome to manage the idx'es
#=================================================
# Implement your function below.
def common_elements(list1, list2):
    result = []

    n1 = len(list1)
    n2 = len(list2)

    idx1 = 0
    idx2 = 0
    
    while 1:
        #print('idx1: {} elem1: {},     idx2: {} elem2: {}'.format(idx1, list1[idx1], idx2, list2[idx2]))
        print('idx1: {},     idx2: {}'.format(idx1, idx2))
        if list1[idx1] == list2[idx2]:
            result.append(list1[idx1])
            print('    common element: {}'.format(list1[idx1]))
            if idx1 < (n1 - 1):
                idx1 += 1
            if idx2 < (n2 - 1):
                idx2 += 1
            
        elif list1[idx1] > list2[idx2]:
            if idx2 < (n2 - 1):
                idx2 += 1
            # list2 has reached the end
            elif idx2 == (n2 - 1) and idx1 < (n1 - 1):
                idx1 += 1
        else:
            if idx1 < (n1 - 1):
                idx1 += 1
            # list1 has reached the end
            elif idx1 == (n1 - 1) and idx2 < (n2 - 1):
                idx2 += 1
                
        # when both the lists reached the end
        if idx1 >= (n1 - 1) and idx2 >= (n2 - 1):
            break
            
    return result


if __name__ == '__main__':
    # NOTE: The following input values will be used for testing your solution.
    list_a1 = [1, 3, 4, 6, 7, 9]
    list_a2 = [1, 2, 4, 5, 9, 10]
    # common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).
    res = common_elements2(list_a1, list_a2)
    print('For {} and {} common elements are: {}\n\n'.format(list_a1, list_a2, res))
    
    list_b1 = [1, 2, 9, 10, 11, 12]
    list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
    # common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).
    res = common_elements2(list_b1, list_b2)
    print('For {} and {} common elements are: {}\n\n'.format(list_b1, list_b2, res))
    
    #'''
    list_c1 = [0, 1, 2, 3, 4, 5]
    list_c2 = [6, 7, 8, 9, 10, 11]
    # common_elements(list_b1, list_b2) should return [] (an empty list).
    res = common_elements2(list_c1, list_c2)
    print('For {} and {} common elements are: {}\n\n'.format(list_c1, list_c2, res))
    #'''
