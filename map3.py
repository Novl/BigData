#!/usr/bin/python

import sys

if __name__ == '__main__':
    with open('quantiles') as borders:
        min_prodTime = float(next(borders))
        max_prodTime = float(next(borders))
    # min_prodTime = 20011992.7097
    # max_prodTime = 20029357.305

    for i in sys.stdin:
        line = i.split(',')
        antiNucleus = int(line[0])
        prodTime = float(line[10])
        Pt_value = float(line[11])
        if min_prodTime <= prodTime <= max_prodTime:
            print(str(antiNucleus) + '\t' + str(Pt_value))
