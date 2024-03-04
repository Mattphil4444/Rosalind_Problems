
a = 4615
b = 8915

n = range(a,b+1)

x = 0

for i in n:
    if i % 2 == 1:
        x = x + i

print(x)