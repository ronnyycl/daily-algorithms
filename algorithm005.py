print('   #\n  ##\n ###\n####\n')


symbol = '#'
space = ' '
n = 6
number_spaces = n-1

for i in range(1, n+1):
    print(f'{space*number_spaces}{symbol*i}')
    number_spaces -= 1
