a = 40
b = 2

x = [1,1]

for i in range(a):
    if i > 1:
        x.append(x[i-2] * b + x[i-1])

print(x[-1:])

