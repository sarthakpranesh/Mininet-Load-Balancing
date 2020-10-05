import csv
#import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

f = open("./log-c1.txt")
data = []
for i in range(1,4):
	f = open("./log-c"+str(i)+".txt")
	c = []
	for row in csv.reader(f):
		c.append(float(row[0])*1000)
	data.append(c)	

x = np.linspace(0,2, 100)

fig, ax = plt.subplots()
ax.plot(data[0], data[0], label="c1")

print("qwertyuiop")
