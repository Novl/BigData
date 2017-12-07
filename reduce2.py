import sys

if __name__ == '__main__':
    i = next(sys.stdin)
    line = i.split('\t')
    antiNucleus = int(line[0])
    eventFile = int(line[1])
    count_distinct = 1
    for i in sys.stdin:
        line = i.split('\t')
        new_antiNucleus = int(line[0])
        new_eventFile = int(line[1])
        if new_antiNucleus == antiNucleus:
            if new_eventFile == eventFile:
                pass
            else:
                eventFile = new_eventFile
                count_distinct += 1
        else:
            print(str(antiNucleus) + ' ' + str(count_distinct))
            antiNucleus = new_antiNucleus
            count_distinct = 1

    print(str(antiNucleus) + ' ' + str(count_distinct))
