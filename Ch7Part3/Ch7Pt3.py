# Week 12, ICA 1
def main():
    marcel = get_goals('dionne.txt')
    total = get_total(marcel)
    print('Marcel Dionne scored',total, 'goals in', len(marcel),'NHL')
    bossy1 = [53, 69, 51, 68, 64, 60, 51, 58, 61, 38]
    store_goals(bossy1, 'bossy1.txt')
    mike = get_data('bossy1.txt', 'bossy2.txt', 10)
    display_data('Mike Bossy', mike, len(mike))

def get_goals(filename):
    goals = [] # empty array
    file = open(filename, 'r')
    goals = file.readlines()    # reads contents of file into list
    file.close()
    index = 0
    while index < len(goals):
        goals[index] = int(goals[index].rstrip('\n'))
        index += 1
    return goals

def get_total(a):
    total = 0
    for num in a:
        total += num
    return total

def store_goals(g, filename):
    file = open(filename, 'w')
    for num in g:
        file.write(str(num)+'\n')
    file.close()

def get_data(file1, file2, rows):
    data = []
    for x in range(rows):
        data.append([0, 0])
    goals = open(file1, 'r')
    assists = open(file2, 'r')
    index = 0
    while index < rows:
        data[index][0] = goals.readline().rstrip('\n')
        data[index][1] = assists.readline().rstrip('\n')
        index += 1
    goals.close()
    assists.close()
    return data

def display_data(name, data, rows):
    print('Career stats for', name)
    print('Goals\tAssists')
    print('---------------')
    for x in range(rows):
        print(f'{data[x][0]}\t\t{data[x][1]}')

# Don't forget to call main
main()