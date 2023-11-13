input=[23,765,9876,54,734]
output=[]
for i in input:
    sum=0
    for digit in str(i):
        sum+=int(digit)
    output.append(sum)
print(output)