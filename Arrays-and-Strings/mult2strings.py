#!/usr/bin/python

class mult:
    def __init__(self, s1, s2):
        print('multiply 2 strings: {} x {}'.format(s1, s2))
        self.s1 = s1
        self.s2 = s2

    def product(self):
        if self.s1 == '0' or self.s2 == '0':
            return '0'
        elif self.s1 == 1:
            return self.s2
        elif self.s2 == 1:
            return self.s1

        ans = [0] * (len(s1) + len(s2))
        print('initial ans: {}'.format(ans))

        for i in range(len(s1) - 1, -1, -1):
            carry = 0
            # Now maintain array position
            k = (len(s1) + len(s2) - 1) - ((len(s1) - 1) - i)
            print('ans position k = {}'.format(k))

            for j in range(len(s2) - 1, -1, -1):
                d1 = int(s2[j])
                d2 = int(s1[i])
                m = (d1 * d2) + carry
                q = m // 10 # this will add to the carry
                r = m % 10  # this should go the the array ans[k]
                print('    {} x {} = {}'.format(d1, d2, m))
                print('    q = {}  r = {}'.format(q, r))

                print('    previous ans[k] = {}, r = {}, q = {}'.format(ans[k], r, q))
                sum_at_k = ans[k] + r #previous value at ans[k] + r
                carry = q + (sum_at_k // 10) # new carry 
                ans[k] = sum_at_k % 10
                print('    ans = {}, carry = {}'.format(ans, carry))

                k -= 1

            if carry > 0:
                ans[k] = carry
                print('        level->ans = {}, carry = {}'.format(ans, carry))

        # process the array ans[] and return the product as a string
        prod = ''
        print('ans: {}'.format(ans))
        for i in ans:
            prod += str(i)

        # trim any 0's from the left
        prod = prod.lstrip('0')
        return prod




if __name__ == '__main__':
    s1 = '34'
    s2 = '34'
    mu = mult(s1, s2)
    prod = mu.product()
    print('product = {}'.format(prod))
