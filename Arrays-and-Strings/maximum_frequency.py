"""
Find the most frequently occuring item in the array.
The item will be unique
For an empty array return None
"""


# Implement your function below.
def most_frequent(given_list):
    max_item = None
    if given_list:
        d = {}
        mf = 0
        for item in given_list:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
                
            if d[item] > mf:
                mf = d[item]
                max_item = item
                
    return max_item

if __name__ == '__main__':
    # NOTE: The following input values will be used for testing your solution.
    # most_frequent(list1) should return 1
    list1 = [1, 3, 1, 3, 2, 1]
    ret = most_frequent(list1)
    print('In list: {} most frequent item = {}'.format(list1, ret))

    # most_frequent(list2) should return 3
    list2 = [3, 3, 1, 3, 2, 1]
    ret = most_frequent(list2)
    print('In list: {} most frequent item = {}'.format(list2, ret))

    # most_frequent(list3) should return None
    list3 = []
    ret = most_frequent(list3)
    print('In list: {} most frequent item = {}'.format(list3, ret))

    # most_frequent(list4) should return 0
    list4 = [0]
    ret = most_frequent(list4)
    print('In list: {} most frequent item = {}'.format(list4, ret))

    # most_frequent(list5) should return -1
    list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
    ret = most_frequent(list5)
    print('In list: {} most frequent item = {}'.format(list5, ret))

