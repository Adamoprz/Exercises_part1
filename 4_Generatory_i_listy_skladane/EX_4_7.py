three_d = [
[[1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]],
[[1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]]
]

#przefiltruj ją tak, by znalazły się tylko te najbardziej wewnętrzne listy, których ilość elementów przekracza 4.
#wynik [[0, -1, -2, -3, -4, -5, -6], [1, 10, 15, 1, 20, 20, 20], [-15, -13, 14, 20, -1]]

reduced = list(map(lambda x: (list(filter(lambda y: len(y)>4, x))), three_d ))


print(reduced)