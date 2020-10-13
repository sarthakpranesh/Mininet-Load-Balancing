import csv
import matplotlib.pyplot as plt
import numpy as np

data = []

load = []
bal = []
for i in range(0, 100):
        load.append(0.0)
	bal.append(0.0)

for i in range(1,4):
	fload = open("./log/log-c"+str(i)+"-load.txt")
	fbal = open("./log/log-c"+str(i)+"-bal.txt")
	j = 0
	for row in csv.reader(fload):
		load[j] = load[j] + float(row[0])*1000
	j = 0
	for row in csv.reader(fbal):
		bal[j] = bal[j] + float(row[0])*1000

for i in range(0, 100):
	load[i] = load[i]/3
	bal[i] = bal[i]/3

data.append(load)
data.append(bal)	

f = open("./log/log-local.txt")
c = []
for row in csv.reader(f):
	c.append(float(row[0])*1000)

data.append(c)

x = np.linspace(0,len(data[0]), len(data[0]))
for i in data:
	plt.plot(x, i)

s = "On load - three clients"
plt.legend(['Non-Balanced under load', 'Balanced under load', 'Off Load'], prop={'size': 6})	
plt.xlabel("Number of Requests")
plt.ylabel("Avergae Response Time (ms)")
plt.show()

print("qwertyuiop")
