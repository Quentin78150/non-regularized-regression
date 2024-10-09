import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_file = './data_lab1 - copie.txt'

columns = ['x','y']

dataset = pd.read_csv(data_file,names = columns, sep=' ')


dataset.plot(kind='scatter',x='x',y='y',color='blue')

plt.show()

print(dataset)