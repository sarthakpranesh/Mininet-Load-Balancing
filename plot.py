import csv
import matplotlib.pyplot as plt
import numpy as np

data = []
for i in range(1,4):
	f = open("./log/log-c"+str(i)+".txt")
	c = []
	for row in csv.reader(f):
		c.append(float(row[0])*1000)
	data.append(c)	

f = open("./log/log-local.txt")
c = []
for row in csv.reader(f):
	c.append(float(row[0])*1000)
data.append(c)

x = np.linspace(0,len(data[0]), len(data[0]))
for i in data:
	plt.plot(x, i)

s = "On load - three clients"
plt.legend([s,s,s,'Off Load - single client'])	
plt.xlabel("Number of Requests")
plt.ylabel("Response Time (ms)")
plt.show()

print("qwertyuiop")
