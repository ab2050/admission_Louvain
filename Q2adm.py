def reach(adl,n):
    rch = [n]
    if adl[n]:
        for i in range(len(adl[n])):
            rch.append(adl[n][i])
            j = adl[n][i]
            rch.extend(adl[j])
    
    rch = set(rch)
    return rch

adl = [[1, 3], [2], [0], [4], [3], []]
n = 0
rch = reach(adl,n)
print(rch)