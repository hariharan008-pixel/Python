import pandas as pd
import numpy as np

a=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print("original dataframe : \n", pd.DataFrame(a))

column=["a","b","c","d","e"]
index1=["A","B"]

print("dataframe after indexing : \n", pd.DataFrame(data = a,index = index1, columns = column))