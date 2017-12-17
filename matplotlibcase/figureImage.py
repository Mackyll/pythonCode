import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
# num代表的是窗口的标题，figsize代表的是窗口的宽度比例
plt.figure(num="lll", figsize=(5, 5), )
# plot函数用来增加一个数学表达式的显示
plt.plot(x, y2, label="image1")
plt.plot(x, y1, color="red", label="image2", linewidth=1.0, linestyle="--")
# 添加图例
plt.legend(loc="upper right")

# 添加一个注视线条
x0 = 1
y0 = 2 * x0 + 1
plt.plot([x0, x0, ], [0, y0, ], 'k--', linewidth=2.5)
# 添加散点
plt.scatter([x0, ], [y0, ], s=20, color='b')

# 给某一个点添加标记
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.show()
