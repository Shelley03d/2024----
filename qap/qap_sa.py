import numpy as np
import random
import math
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

# 计算总费用
def cost(solution, h, d):
    total_cost = 0
    for i in range(len(solution)):
        for j in range(len(solution)):
            total_cost += h[i][j] * d[solution[i]][solution[j]]
    return total_cost

# 生成新的解决方案
def generate_solution(current_solution):
    new_solution = current_solution[:]
    i, j = random.sample(range(len(new_solution)), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# 模拟退火
def simulated_annealing(n, h, d, initial_temperature, cooling_rate):
    current_solution = list(range(n))  # 初始解决方案
    current_cost = cost(current_solution, h, d)

    for t in range(1, 10000):
        temperature = initial_temperature / math.log(t+1)
        new_solution = generate_solution(current_solution)
        new_cost = cost(new_solution, h, d)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_solution, current_cost = new_solution, new_cost
        if temperature < 0.01:
            break

    return current_solution, current_cost

# 读取数据并运行模拟退火算法
data = read_data_from_folder('E:/project/2024/2024-buaa-kykt-intelligent-computing/qap/qap-problems')
for n, h, d in data:
    best_solution, best_cost = simulated_annealing(n, h, d, 1000, 0.99)
    print('Best solution:', best_solution)
    print('Best cost:', best_cost)