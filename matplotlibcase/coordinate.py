import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, 100)
y = x ** 2
plt.figure()
# 设置y轴的范围
plt.ylim(-10, 10)
# 设置x轴的范围
plt.xlim(-5, 20)
# 设置y轴的标签
plt.ylabel("testy")
# 设置x轴的标签
plt.xlabel("testx")
# 设置刻度
new_tickes = np.linspace(-5, 20, 5)
# 给每个刻度设置一个label
plt.xticks(new_tickes, ["label1", "label2", "label3", "label4"])
# 设置坐标轴的位置和颜色
ax = plt.gca()
ax.spines['right'].set_color('red')
ax.spines['top'].set_color('blue')
ax.spines['bottom'].set_position(("data", 0))
plt.plot(x, y)
plt.show()
