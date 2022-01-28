#!/home/studentb07/.local/share/virtualenvs/sprawozdanie-5D_5EEiY/bin/python

import pandas as pd

read_file = pd.read_csv (r'zad2b.txt',header=None)
read_file.columns = ["Rok", "Ludnosc"]
read_file.to_csv (r'zad2b.csv', index=None)

import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('zad2b.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()