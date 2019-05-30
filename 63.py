s=input()
l=list(s)
le=len(l)
r=[]
for i in range(le):
    if(l[i] not in r):
        r.append(l[i])
count=0
rl=len(r)
for i in range(rl):
    if(r[i]==l[i]):
        count+=1
print(count)
