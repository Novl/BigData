import sys

if __name__ == '__main__':
    i = next(sys.stdin)
    line = i.split('\t')
    antiNucleus = int(line[0])
    Pt_sum = float(line[1])
    Pt_count = 1
    for i in sys.stdin:
        line = i.split('\t')
        new_antiNucleus = int(line[0])
        new_Pt_value = float(line[1])
        if new_antiNucleus == antiNucleus:
            Pt_sum += new_Pt_value
            Pt_count += 1
        else:
            print(str(antiNucleus) + ' ' + str(Pt_sum/Pt_count))
            antiNucleus = new_antiNucleus
            Pt_sum = new_Pt_value
            Pt_count = 1

    print(str(antiNucleus) + ' ' + str(Pt_sum/Pt_count))
