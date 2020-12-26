elements = []
for i in range(2,20):
    cp = i
    for j in range(len(elements)):
        if cp % elements[j] == 0:
            cp //= elements[j]
            if cp == 1:
                break
    else:
        elements.append(cp)

mul = 1
for k in range(len(elements)):
    mul *= elements[k]

print(mul)
