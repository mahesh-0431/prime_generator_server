def prime(start,end):
    res=[]
    for i in range(start,end+1):
        c=0
        for j in range(1,(i//2)+1):
            if i%j==0:
                c+=1
        if c==1:
            res.append(i)
    return res

def mahi(start,end):
    res=[]
    for i in range(start,end+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            res.append(i)
    return res
