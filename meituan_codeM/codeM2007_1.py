# coding = utf-8
# user   = hu_yang_jie

import os
import time


def f1():
    in_str = input()
    l, r = int(in_str.split(' ')[0]), int(in_str.split(' ')[1])
    num_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i in range(l, r+1):
        if i%2 == 0:
            for h in range(2, r+1, 2):
                if i % h == 0:
                    num_dict[int(str(h)[0])] += 1
        else:
            for h in range(1, r+1):
                if i % h == 0:
                    num_dict[int(str(h)[0])] += 1
    for k in range(1, 10):
        print(num_dict[k])


def f2():
    import sys

    def solve(r):
        ans = [0] * 10
        for u in range(1, 10):
            v = 1
            while u * v <= r:
                s = u * v
                e = min(s + v - 1, r)
                i = s
                while i <= e:
                    mult, rema = divmod(r, i)
                    slip = 1 + min(rema // mult, e - i)
                    ans[u] += mult * slip
                    i += slip
                v *= 10
        return ans

    l, r = [int(s) for s in input().split(' ')]
    ans1 = solve(l - 1)
    ans2 = solve(r)
    for i in range(1, 10):
        print(ans2[i] - ans1[i])


if __name__ == '__main__':
    f1()
