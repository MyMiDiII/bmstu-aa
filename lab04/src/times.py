import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

plt.figure(figsize=(15.5, 9))
plt.subplots_adjust(hspace=0.5)
plt.subplot(1, 2, 1)
labels = ['последовательный', 'параллельный']
xVals = [1, 2, 4, 8, 16, 32]
sVals = [880622058] * 6
pVals = [ 839013147,
          446833477,
          338605815,
          300881333,
          317716474,
          622792430
#         1561156672
        ]

plt.plot(xVals, sVals, label=labels[0])
plt.plot(xVals, pVals, label=labels[1])

plt.xlabel("Количество потоков", fontsize=14)
plt.ylabel("Время, ns", fontsize=14)
plt.grid(True)
plt.legend()

ax = plt.subplot(1, 2, 2)
labels = ['последовательный', '8 потоков']
# ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

xVals = [i for i in range(4, 8)]
ax.set_xticks(xVals)
ax.xaxis.set_major_formatter(FixedFormatter(xVals))
sVals = [#    167321,
         #   1063368,
         #   8724506,
           23780663,
          849861484,
         1701109328,
         2549415743
        ]
pVals = [#  24051708,
         # 161824161,
         # 264771774,
          364664568,
          666893339,
          967859493,
         1272447909
        ]

plt.plot(xVals, sVals, label=labels[0])
plt.plot(xVals, pVals, label=labels[1])

plt.xlabel("Число знаков после запятой", fontsize=14)
plt.ylabel("Время, ns", fontsize=14)
plt.grid(True)
plt.legend()

plt.get_current_fig_manager().window.move(0, 0)
plt.show()
