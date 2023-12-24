import numpy as np

def task(a,b):
    # a=np.array([[1,5,3,9],[5,7,2,8],[6,1,0,4]])
    # b=np.array([[5,8,7,6],[9,4,3,8],[1,7,3,6]])
    c=a*b
    print("\n Sum : ", a+b)
    print("\n Difference : ", a-b)
    print("\n Product : ", a*b)
    print("\n Divide : ", a/b)
    print("\n C : ", c)
    print("\n Indexing : ", c[-2])
    print("\n Slicing : ", c[0:2])
    print(" \n Sorting : ", np.sort(c))
    
    return c

if __name__ == "__main__": 
    print ("Executed when invoked directly")
    a=np.array([[1,5,3,9],[5,7,2,8],[6,1,0,4]])
    b=np.array([[5,8,7,6],[9,4,3,8],[1,7,3,6]])
    task(a,b)
else: 
    print ("Executed when imported")