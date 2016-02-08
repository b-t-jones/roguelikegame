import numpy 
import matplotlib.pyplot as pyplot
import numpy.random
from scipy.interpolate import spline

x = numpy.arange(16)
y = numpy.zeros(16)
for i in range(15):
	y[i+1]= numpy.random.rand(1)
print y

xnew = numpy.linspace(x.min(),x.max(),300)
power_smooth = spline(x,y,xnew)


pyplot.figure(figsize=(8,4))
pyplot.plot(xnew,power_smooth)
pyplot.grid(axis='y', linestyle='')
pyplot.grid(axis='x', linestyle='')
pyplot.yticks([1])
pyplot.xticks(x)
pyplot.ylim([0,1])


pyplot.figure(figsize=(8,4))
pyplot.xlabel("")
pyplot.ylabel("")
pyplot.grid(True)
pyplot.plot(x,y, linestyle='', marker='x')
pyplot.yticks([1])
pyplot.xticks(x)
pyplot.grid(axis='y', linestyle='')
pyplot.grid(axis='x', linestyle='')
# pyplot.plot(xs, df_good_dx - numpy.cos(xs), label = "dx = pi*e-2")
# pyplot.plot(xs, df_large_dx - numpy.cos(xs), label = "dx = pi*1.5")
# pyplot.legend(loc='lower right')

pyplot.show()