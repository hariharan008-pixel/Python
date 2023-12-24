import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Multiple Plots
# With the subplot() function you can draw multiple plots in one figure:

# Draw 2 plots:

def sub1(a,b,x,y):
    
    #plot1
    plt.subplot(1,2,1)              # the figure has 1 row, 2 columns, and this plot is the first plot.
    plt.plot(a,b)
    
    #plot2
    plt.subplot(1,2,2)              # the figure has 1 row, 2 columns, and this plot is the second plot.
    plt.plot(x,y)           
    
    plt.suptitle("Companies")
    plt.show()
    
a=np.array([54,98,65,87])
b=np.array([32,54,76,43])
x=np.array([76,23,78,45])
y=np.array([76,56,98,23])

sub1(a,b,x,y)

# Draw 2 plots on top of each other:

def sub2(a,b,x,y):
    
    #plot1
    plt.subplot(2,1,1)              # the figure has 2 row, 1 columns, and this plot is the first plot.
    plt.plot(a,b)
    
    #plot2
    plt.subplot(2,1,2)              # the figure has 2 row, 1 columns, and this plot is the second plot.
    plt.plot(x,y)           
    
    plt.suptitle("Companies")
    plt.show()
    
a=np.array([54,98,65,87])
b=np.array([32,54,76,43])
x=np.array([76,23,78,45])
y=np.array([76,56,98,23])

sub2(a,b,x,y)

# Draw 6 plots on top of each other:

def sub2(a,b,x,y):
    
    #plot1
    plt.title("TCS")
    plt.subplot(2,3,1)              # the figure has 2 row, 3 columns, and this plot is the first plot.
    plt.plot(a,marker="*",ls=":",mec="k")
    plt.plot(b,marker="o",ls="--",mec="k")
    
    #plot2
    plt.title("HCL")
    plt.subplot(2,3,2)              # the figure has 2 row, 3 columns, and this plot is the second plot.
    plt.plot(x,marker="d",ls="-.",mec="k",c="r")
    plt.plot(y,marker="D",ls="-",mec="k",c="g")          
    
    #plot3
    plt.title("CTS")
    plt.subplot(2,3,3)              # the figure has 2 row, 3 columns, and this plot is the third plot.
    plt.plot(a,marker="p",ls=":",mec="k",c="b")
    plt.plot(b,marker="h",ls="-.",mec="k",c="c")
    
    #plot4
    plt.title("INFOSYS")
    plt.subplot(2,3,4)              # the figure has 2 row, 3 columns, and this plot is the fourth plot.
    plt.plot(x,marker="<",ls="--",mec="k",c="m")  
    plt.plot(y,marker=">",ls=":",mec="k",c="y")
    
    #plot5
    plt.title("CAPGEMINI")
    plt.subplot(2,3,5)              # the figure has 2 row, 3 columns, and this plot is the fifth plot.
    plt.plot(a,marker="1",ls="-",mec="k",c="k")
    plt.plot(b,marker="2",ls="--",mec="k",c="g")
    
    #plot6
    plt.title("ZOHO")
    plt.subplot(2,3,6)              # the figure has 2 row, 3 columns, and this plot is the sixth plot.
    plt.plot(x,marker="3",ls=":",mec="k",c="r") 
    plt.plot(y,marker="4",ls="-",mec="k",c="c")
    
    plt.suptitle("Companies")
    plt.xlabel("Year")
    plt.ylabel("Hike")
    plt.show()
    
a=np.array([54,98,65,87])
b=np.array([32,54,76,43])
x=np.array([76,23,78,45])
y=np.array([76,56,98,23])

sub2(a,b,x,y)





