import sys

if __name__ == '__main__':
    for i in sys.stdin:
        line = i.split(',')
        prodTime = float(line[10])
        print('1\t'+str(prodTime))
