import pandas as pd

a=[7654,9875,2345,8765]
x=pd.Series(a)
print(x.to_frame())