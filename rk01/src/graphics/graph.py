import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

plt.figure(figsize=(15.5, 9))
plt.subplots_adjust(hspace=0.5)
plt.subplot(1, 2, 1)

label = 'Вторая лента'
xVals = [i for i in range(10, 820, 100)]
tVals = [31  * 10 ** 6,
         113 * 10 ** 6,
         226 * 10 ** 6,
         373 * 10 ** 6,
         431 * 10 ** 6,
         632 * 10 ** 6,
         867 * 10 ** 6,
         883 * 10 ** 6,
         936 * 10 ** 6]

plt.plot(xVals, tVals, label=label)

plt.xlabel("Разброс, ns", fontsize=14)
plt.ylabel("Время, ns", fontsize=14)
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
label = 'Третья лента'

tVals = [36   * 10 ** 6,
         387  * 10 ** 6,
         489  * 10 ** 6,
         545  * 10 ** 6,
         797  * 10 ** 6,
         1.16 * 10 ** 9,
         1.38 * 10 ** 9,
         1.6  * 10 ** 9,
         1.94 * 10 ** 9]

plt.plot(xVals, tVals, label=label)

plt.xlabel("Разброс, ns", fontsize=14)
plt.ylabel("Время, ns", fontsize=14)
plt.grid(True)
plt.legend()

plt.get_current_fig_manager().window.move(0, 0)
plt.show()
