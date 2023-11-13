input=[32,54,76,72]
a=input[0]
input[0]=input[-3]
input[-3]=a
print(input)