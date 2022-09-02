colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

#zmiana na ['red pink', 'white black', 'orange green']

colors_2 = list(map(lambda x: x[0] + ' ' + x[1], colors))

print(colors_2)