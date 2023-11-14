input=(1,2,3,4,5,6)
output=[]
for i in range(len(input)-1):
    res=input[i]*input[i+1]
    output.append(res)
print(tuple(output))