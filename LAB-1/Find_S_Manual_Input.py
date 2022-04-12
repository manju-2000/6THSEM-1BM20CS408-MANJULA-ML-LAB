import pandas as pd #supports for multi dimensional array # built on top of Numpy
import numpy as np


Row=int(input("Ënter the number of rows:"))
C = int(input("Enter the number of columns:"))
 
# Initialize matrix
data = []
print("Enter the entries rowwise:")
 
# For user input
for i in range(Row):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(input())
    data.append(a)
 
print(data)


d = np.array(data)[:, :-1]
print("n The attributes are: ", d)


target = np.array(data)[:, -1]
print("n The target is: ", target)

def FindS(c, t):
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            print("sh is ", specific_hypothesis)
            break

    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass

    return specific_hypothesis


# obtaining the final hypothesis
print("n The final hypothesis is:", FindS(d, target))
