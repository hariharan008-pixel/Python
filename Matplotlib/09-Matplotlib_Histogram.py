import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Histogram
# A histogram is a graph showing frequency distributions.
# It is a graph showing the number of observations within each given interval.
# Example: You can read from the histogram that there are approximately:
# 2 people from 140 to 145cm
# 5 people from 145 to 150cm
# 15 people from 151 to 156cm

# A Normal Data Distribution by NumPy:

def hist1(a):
    
    plt.hist(a)
    plt.show()
    
a=np.random.normal(170,10,250)

hist1(a)

def hist2(x,y):
    
    plt.hist(x)
    plt.hist(y)
    
    plt.show()
        
x=np.random.normal(40,5,100)
y=np.random.normal(30,10,100)

hist2(x,y)