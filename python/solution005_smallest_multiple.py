elements = []
for i in range(2,20):
    for v in elements:
        q, r = divmod(i, v)
        if not r:
            i = q
            if i == 1:
                break
    else:
        elements.append(i)

mul = 1
for v in elements:
    mul *= v

print(mul)
