a=input().split(',')
b=a
e=d=0
r=[]
c=b[0][-1]
r.append(b[0])
b.remove(b[0])
b.sort()
for i in range(1,len(a)+1):
    for j in b:
        e=0
        if c==j[0]:
            r.append(j)
            b.remove(j)
            c=j[-1]
            e+=1
        if e==1:
            break
print(r)
