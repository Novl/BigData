#!/usr/bin/python

import sys

if __name__ == '__main__':
    i = next(sys.stdin)
    line = i.split('\t')
    max_prodTime = float(line[1])
    min_prodTime = float(line[1])
    for i in sys.stdin:
        line = i.split('\t')
        prodTime = float(line[1])
        if max_prodTime < prodTime:
            max_prodTime = prodTime
        if min_prodTime > prodTime:
            min_prodTime = prodTime
    # print(min_prodTime)
    # print(max_prodTime)
    print(min_prodTime + (max_prodTime - min_prodTime) * 0.05)
    print(max_prodTime - (max_prodTime - min_prodTime) * 0.05)
    # print(min_prodTime + (max_prodTime - min_prodTime) * 0.05, max_prodTime - (max_prodTime - min_prodTime) * 0.05)