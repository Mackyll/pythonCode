import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
# num代表的是窗口的标题，figsize代表的是窗口的宽度比例
plt.figure(num="lll", figsize=(5, 5), )
# plot函数用来增加一个数学表达式的显示
plt.plot(x, y2)
plt.plot(x, y1, color="red", linewidth=1.0, linestyle="--")
plt.show()
