a=[8,7,1,2,3,4,5,6,4,4,5,6,7,8]
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
print((b))