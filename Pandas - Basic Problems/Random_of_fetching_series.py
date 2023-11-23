import pandas as pd
import random

x=[]
for i in range(5):
    a=random.randint(2,9)
    x.append(a)
print(pd.Series(x))