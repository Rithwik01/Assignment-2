
#Question 1

import numpy as np

num=np.random.randint(1,51, size=(100,10))

print(num.mean())
print(np.median(num))
print(num.std())
print(np.max(num))



#Question 2

arr = np.random.randint(low=1, high=51, size=(1000,)) 
diff = arr[-1] - arr[0]
print(arr) #prints the whole array
print(arr[:10]) #prints the first 10 numbers in the array
print(arr[-10:]) #prints the last 10 numbers in the array
print(np.var(arr))  #prints the variance
print(np.diff(arr)) #Calculates the adjacent number in the array
print(diff) #Calculates the difference in the array
arr.sort() #sorts the array
print(arr[:10]) #first 10 after sort
print(arr[-10:]) #last 10 after sort
print(np.var(arr))#variance of the sorted array
print(arr[0:10].mean()) #prints the mean of the first 10
print(arr[-10:].mean()) #prints the mean of the last 10




