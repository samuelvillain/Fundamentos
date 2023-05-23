a = [3, 2, 4]
b = [5, 2, 4]
c = [0, 0, 0]

for multiplicacao in range(len(a)):
    c[multiplicacao] = a[multiplicacao] * b[multiplicacao]

print(c)