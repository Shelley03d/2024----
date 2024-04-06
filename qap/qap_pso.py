import numpy as np
import random
import os

def read_data_from_folder(folder_name):
    data = []
    for file_name in os.listdir(folder_name):
        if file_name.endswith('.dat'):
            with open(os.path.join(folder_name, file_name), 'r') as file:
                n = int(file.readline())
                h = np.zeros((n, n))
                d = np.zeros((n, n))
                for i in range(n):
                    line = file.readline()
                    while not line.strip():  # 跳过空行
                        line = file.readline()
                    h[i] = list(map(int, line.split()))
                for i in range(n):
                    line = file.readline()
                    while not line.strip():  # 跳过空行
                        line = file.readline()
                    d[i] = list(map(int, line.split()))
                data.append((n, h, d))
    return data

# 粒子类
class Particle:
    def __init__(self, size, pmin, pmax, smin, smax):
        self.position = random.sample(range(pmin, pmax), size)
        self.velocity = [random.uniform(smin, smax) for _ in range(size)]
        self.best_position = self.position
        self.best_score = float('inf')

def map_position_to_integers(position):
    # 初始化整数序列
    integers = list(range(len(position)))

    # 创建一个由(position[i], i)组成的元组列表
    tuples = [(position[i], i) for i in range(len(position))]

    # 根据position[i]的值对元组列表进行排序
    tuples.sort()

    # 创建一个到整数序列的映射
    mapping = {tuples[i][1]: integers[i] for i in range(len(tuples))}

    # 使用映射更新位置
    return [mapping[i] for i in range(len(position))]

# 适应度函数
def fitness(position):
    position = map_position_to_integers(position)
    s = 0.0
    for i in range(n):
        for j in range(n):
            s += h[i][j] * d[position[i]][position[j]]
    return s

# 更新粒子
def update_particle(particle, best_particle, phi1=2.0, phi2=2.0):
    for i in range(n):
        u1 = random.uniform(0, phi1)
        u2 = random.uniform(0, phi2)
        particle.velocity[i] = particle.velocity[i] + u1 * (particle.best_position[i] - particle.position[i]) + u2 * (best_particle.position[i] - particle.position[i])
        particle.position[i] += particle.velocity[i]

# 粒子群优化
def pso(n,h,d,pop_size=100, max_iter=100):
    particles = [Particle(n, 0, n, -3, 3) for _ in range(pop_size)]
    best_particle = min(particles, key=lambda p: fitness(p.position))

    for _ in range(max_iter):
        for particle in particles:
            update_particle(particle, best_particle)
            score = fitness(particle.position)
            if score < particle.best_score:
                particle.best_score = score
                particle.best_position = particle.position
        best_particle = min(particles, key=lambda p: fitness(p.position))

    return best_particle.position

data = read_data_from_folder('E:/project/2024/2024-buaa-kykt-intelligent-computing/qap/qap-problems')
for n, h, d in data:
    best_position = pso(n, h, d)
    best_position = map_position_to_integers(best_position) # 将位置映射为整数
    print('Best position:', best_position)