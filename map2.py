import sys
# from __future__ import print_function

if __name__ == '__main__':
    # with open('quantiles.txt') as borders:
    #     min_prodTime = float(next(borders))
    #     max_prodTime = float(next(borders))
    min_prodTime = 20011992.7097
    max_prodTime = 20029357.305

    for i in sys.stdin:
        line = i.split(',')
        antiNucleus = int(line[0])
        eventFile = int(line[1])
        prodTime = float(line[10])
        if min_prodTime <= prodTime <= max_prodTime:
            print(str(antiNucleus) + '\t' + str(eventFile))
