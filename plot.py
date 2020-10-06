import csv
import matplotlib.pyplot as plt
import numpy as np

data = []
for i in range(1,4):
	f = open("./log-c"+str(i)+".txt")
	c = []
	for row in csv.reader(f):
		c.append(float(row[0])*1000)
	data.append(c)	

f = open("./log-local.txt")
c = []
for row in csv.reader(f):
	c.append(float(row[0])*1000)
data.append(c)

x = np.linspace(0,len(data[0]), len(data[0]))
for i in data:
	plt.plot(x, i)
	
plt.show()

print("qwertyuiop")
