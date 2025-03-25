import numpy as np
import matplotlib.pyplot as plt


# 设置模型参数
beta = 0.3  # 感染概率
gamma = 0.1  # 恢复概率
num_time_points = 100  # 时间点数


# 初始化人群数组
population = np.zeros((100, 100))


# 引入初始感染个体
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1


# 时间进程模拟
for t in range(num_time_points):
    # 找到感染点
    infected_points = np.where(population == 1)

    # 感染邻居
    for i, j in zip(infected_points[0], infected_points[1]):
        for x in range(max(0, i - 1), min(100, i + 2)):
            for y in range(max(0, j - 1), min(100, j + 2)):
                if (x != i or y != j) and population[x, y] == 0:
                    if np.random.random() < beta:
                        population[x, y] = 1

    # 感染个体恢复
    recovered_points = np.where((population == 1) & (np.random.random(population.shape) < gamma))
    population[recovered_points] = 2

    # 绘制每个时间点的热力图（这里简单打印，如需保存可自行添加代码）
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f"Time point {t}")
    plt.show()