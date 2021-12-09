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

