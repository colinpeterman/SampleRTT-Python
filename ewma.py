import matplotlib.pyplot as plt 
import numpy as np 
import array as arr
""" load sample RTTs into numpy array """
SampleRTT = np.loadtxt("ewma.txt")

""" alpha and beta values """
alpha = 0.9
beta = 0.25
estimated = 0;
dev = 0;
time = 0;

""" TODO: implement EWMA as presented in the class slides,
and store the time out interval values in an array named TimeoutInterval """
TimeoutInterval = arr.array('d',[])

for x in SampleRTT:
	estimated = ((1-alpha)*estimated) + (alpha * x)
	dev = ((1 - beta) * dev) + (beta * abs(estimated - x))
	time = (estimated + (4*dev))
	TimeoutInterval.append(time)


""" Plot sample RTT values, and timeout interval values """
SampleRTT_plt = plt.plot(range(len(SampleRTT)), SampleRTT, color = 'blue', label='SampleRTT')  
TimoutInterval_plt = plt.plot(range(len(SampleRTT)), TimeoutInterval, color = 'red', label='TimeoutInterval')  
plt.xlabel('Samples')
plt.ylabel('RTT (ms)')
plt.legend(loc = 'upper right')
plt.show()
