import pandas as pd

x=pd.read_excel("file2.xlsx",index_col ="Name")
y=x[["Job"]]
z=x.loc[["Hari"]]
print(y)
print(z)