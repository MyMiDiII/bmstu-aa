from prettytable import PrettyTable
import csv
from colored import fg, attr

def printRes(resDict, name):
    if resDict is None:
        print("%sНет такой игры!%s" % (fg('red'), attr(0)))
        return 

    resDict['Name'] = name
    table = PrettyTable()
    table.field_names = list(resDict.keys())[3:] + list(resDict.keys())[:-1]
    table.add_row(list(resDict.values())[3:] + list(resDict.values())[:-1])
    print(table)


def printTable(lens, times, names, align=0):
    table = PrettyTable()
    table.field_names = names
    for i in range(len(lens)):
        table.add_row([lens[i]] + [col[i] for col in times])

    table.align = 'r'
    print(
        align * ' ',
        table.get_string().replace('\n', '\n' + align * ' '),
        sep=''
        )


def printTour(tour):
    print(*tour, sep=' -> ')


def saveTableAsCSV(sizes, times):
    table = zip(sizes, *times)
    with open('../docs/data/csv/times.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['size', 'bf', 'ants'])
        writer.writerows(table)
