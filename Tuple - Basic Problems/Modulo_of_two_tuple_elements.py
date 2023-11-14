tup1=(10,4,5,6)
tup2=(5,6,7,5)
output=[]
for i in range(0,len(tup1)):
    res=(tup1[i]%tup2[i])
    output.append(res)
print(output)