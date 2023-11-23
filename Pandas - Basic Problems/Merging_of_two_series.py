import pandas as pd

a=[765,987,345,765]
b=[2354,8376,3456,7653]
x=pd.Series(a)
y=pd.Series(b)
print(x._append(y))