import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

numpArray = np.array([])
read = pd.read_csv("/Users/rithwikkamalesh/Desktop/Data Science folder/US_population.csv")
#print(read)
population = read[" Population"]
print(population)
array = np.append(numpArray, population)
print(array)
diff = array[-1] - array[0]
print(diff)


plt.plot(population[:60], linestyle="solid")
plt.plot(population[60:], linestyle="dashed")
plt.plot(population[:60])
plt.plot(population[60:])

