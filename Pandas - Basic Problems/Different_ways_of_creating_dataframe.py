import pandas as pd

# #Creating empty dataframe
print("\n empty dataframe : \n", pd.DataFrame())

# #creating dataframe from list
a=[34,987,45,87,34]
print("\n dataframe from list : \n", pd.DataFrame(a))

# #creating dataframe from tuple
a=(34,987,45,87,34)
print("\n dataframe from tuple : \n", pd.DataFrame(a))

#creating dataframe from dictionary
a={"a":"hari","b":"haran"}
print("\n dataframe from dictionary : \n", pd.DataFrame([a]))

#creating dataframe from series
a=(34,987,45,87,34)
x=pd.Series([a])
print("\n dataframe from series : \n", x.to_frame())