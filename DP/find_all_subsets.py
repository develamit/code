"""
Given an integer array, find all subsets
This is a DP problem
Solving it using bottom up approach.
Approach: Take the previous solution + for each item
          in the previous solution, add the current element
"""

def findAllSubsets(list1):
    ret = []
    ret.append([]) # null set

    for i in range(len(list1)):

        temp = []
        #print('begin ret: {}'.format(ret))

        # append the current item to every subset from the previous solution
        for existing_subset in ret:
            # lists are muatble, so better copy it deep. Assignment won't work, since it just copies the reference
            s1 = existing_subset[:]

            if not existing_subset: # dealing with [] null set
                s1 = [list1[i]]
            else:
                s1.append(list1[i])
                #s1 += [list1[i]]

            temp.append(s1)
            #temp += [s1]

        # Now append the current solution to the previous solution
        ret += temp
        #for elem in temp:
            #ret.append(elem)

        #print('ret_cur: {}\n'.format(ret))


    return ret





if __name__=='__main__':
    #list1 = []
    #list1 = [1,2,3]
    list1 = [1,2,3,4,5]
    ret = findAllSubsets(list1)
    print('list: {}, subsets: {}'.format(list1, ret))
