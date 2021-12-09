import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

plt.figure(figsize=(15.5, 9))
plt.subplots_adjust(hspace=0.5)
plt.subplot(1, 2, 1)
labels = ['последовательная', 'конвейерная']

xVals = [5, 10, 25, 50, 75, 100, 250, 500, 750, 1000]
lVals = [  1398118,
           2842780,
           6987262,
          13423468,
          20151882,
          27811972,
          71697350,
         133232370,
         209148024,
         276952383]
pVals = [  1744339,
           2770063,
           5289069,
           8961571,
          13339268,
          17249171,
          40135084,
          84669318,
         127482157,
         160373144]

plt.plot(xVals, lVals, label=labels[0])
plt.plot(xVals, pVals, label=labels[1])

plt.xlabel("Количество заявок", fontsize=14)
plt.ylabel("Время, ns", fontsize=14)
plt.grid(True)
plt.legend()

ax = plt.subplot(1, 2, 2)
ax.set_xticks(xVals)
ax.xaxis.set_major_formatter(FixedFormatter(xVals))
labels = ['последовательная', 'конвейерная']

xVals = [5, 10, 25, 50, 75, 100]
lVals = [ 12787683,
          25006741,
          62884400,
         132833197,
         201132505,
         259405110
        ]
pVals = [  8451608,
          14918758,
          37303679,
          73853581,
         108303512,
         143977382]

plt.plot(xVals, lVals, label=labels[0])
plt.plot(xVals, pVals, label=labels[1])

plt.xlabel("Количество слов", fontsize=14)
plt.ylabel("Время, ns", fontsize=14)
plt.grid(True)
plt.legend()

plt.get_current_fig_manager().window.move(0, 0)
plt.show()
