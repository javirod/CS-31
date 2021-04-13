# Week 10, ICA 1
outfile = open('players.txt', 'w')
outfile.write('Sidney Crosby\n')
outfile.write('John Carlson'+'\n')
outfile.write('Jordan Binnington\n')
outfile.close()
# Append one more name in the file
outfile = open('players.txt','a')
outfile.write('Alex Ovechkin\n')
outfile.close()
outfile = open('numbers.txt','w')
outfile.write(str(89)+'\n')
outfile.write(str(74)+'\n')
outfile.write(str(50)+'\n')
outfile.write(str(8)+'\n')
outfile.close()
# Create input file object
infile1 = open('players.txt','r')
infile2 =  open('numbers.txt','r')
# player = infile1.readline().rstrip('\n')
# num = infile2.readline().rstrip('\n')
# while player!= '' and num != '':
#     print(player, 'wears number', num)
#     player = infile1.readline().rstrip('\n')
#     num = infile2.readline().rstrip('\n')›
for player in infile1:
    player = player.rstrip('\n')
    num = infile2.readline().rstrip('\n')
    print(player, 'wears number', num)

infile1.close()
infile2.close()