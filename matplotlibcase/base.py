import matplotlib.pyplot as plt
import numpy as np

# 生成50个点每个点间隔40
x = np.linspace(-100, 100, 50)
# y也生成对应的50个点
y = 2 * x + 1
plt.figure()
plt.plot(x, y)
plt.show()
