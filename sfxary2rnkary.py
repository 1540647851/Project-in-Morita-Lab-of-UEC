def rnkary(sa,l=0):
    if l==0:
        l=len(sa)
    rank=[]
    for i in range(l):
        rank.append(sa.index(i))
    return rank
