with open('day1_input') as f:
    data = f.readlines()

data = data[0].strip('\n').split(", ")

#part1
x, y = 0, 0
m = [(1, 0), (0, 1), (-1, 0), (0, -1)]
i = 0
for ds in data:
    d = ds[0]
    s = int(ds[1:])
    if d == "R":
        i = (i + 1) % 4
    else:
        i = (i - 1) % 4
    x, y = x + s * m[i][0], y + s * m[i][1]

print(abs(x) + abs(y))

#part2
x, y = 0, 0
m = [(1, 0), (0, 1), (-1, 0), (0, -1)]
i = 0
l = set()
for ds in data:
    d = ds[0]
    s = int(ds[1:])
    if d == "R":
        i = (i + 1) % 4
    else:
        i = (i - 1) % 4
    for k in range(s):
        x, y = x + m[i][0], y + m[i][1]
        if (x, y) in l:
            print(abs(x) + abs(y))
            break
        l.add((x, y))
    else:
        continue
    
    break