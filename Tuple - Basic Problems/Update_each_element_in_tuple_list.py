input=[(1,2,3),(4,5,6),(7,8,9)]
output=[]
for i in input:
    tem1=list(i)
    tem1[2]=0
    tem2=tuple(tem1)
    output.append(tem2)
print(output)