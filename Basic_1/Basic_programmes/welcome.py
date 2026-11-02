s="moourya"
d={}
m=0
h=" "
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    print(v)
    if v>m:
        m=v
        h=k



