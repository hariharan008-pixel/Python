import pandas as pd
import matplotlib.pyplot as plt

out1=pd.read_excel("Test1.xlsx")
x_axis=out1["X value"]
y_axis=out1["Y value"]

plt.plot([x_axis,y_axis])
plt.show()

