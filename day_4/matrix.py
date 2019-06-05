a = [[1,2], [3,7, 6, 'a'], []]

# Iterowanie po zagnieżdżonej liście za pomocą indeksów
for ii in range(len(a)):
    for jj in range(len(a[0])):
        print (f'a[{ii}, {jj}]={a[ii][jj]}')

# I z użyciem funkcji enumerate
for ii, row in enumerate(a):
    for jj, elem in enumerate(row):
       print(f'a[{ii}, {jj}]={elem}')
    print('end of row')