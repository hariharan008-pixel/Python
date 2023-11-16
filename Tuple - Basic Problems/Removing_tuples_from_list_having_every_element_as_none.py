input=[(None, 2), (None, None), (3, 4), (12, 3), (None, )]
output=[]
for i in input:
    if None not in i:
        output.append(i)
print(output)
