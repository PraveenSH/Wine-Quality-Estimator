import matplotlib.pyplot as plt

_Log = open('error.log','r');
error = []
first_line = True;
for line in _Log:
	if first_line:
		first_line = False
		continue
	row = line.split(',')
	diff = float(row[2].split('\n')[0]);
	error.append(diff);

plt.plot(error,'ro');
plt.ylabel('Error')
plt.show()
