input=[2,4,6,8,3,5,7,3,5,7,9,0,1]
org=[]
dup=[]
for i in input:
    if i not in org:
        org.append(i)
for i in org:
    if input.count(i)>1:
        dup.append(i)
print(dup)