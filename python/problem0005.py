elements = []
for i in range(2,20):
    for v in elements:
        if i % v == 0:
            i //= v
            if i == 1:
                break
    else:
        elements.append(i)

mul = 1
for v in elements:
    mul *= v

print(mul)
