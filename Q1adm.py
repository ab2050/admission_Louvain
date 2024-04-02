def mtl(adm):
    adl = []

    for i in range(len(adm)):
        adl.append([])
        for j in range(len(adm[i])):
            if adm[i][j] == 1:
                adl[i].append(j)
    return adl
adm = [
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],]

adl = mtl(adm)
print(adl)
