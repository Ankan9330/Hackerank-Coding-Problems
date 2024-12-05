def permutationqeries(p):
    result= 0
    n =len(p)
    for i in range(1,n+1):
        result.append(p.index(p.index(i)+1)+1)
    return result