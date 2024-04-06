from deap import base, creator, tools, algorithms
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


# 定义适应度函数
def fitness(individual, h, d):
    cost = 0
    for i in range(len(individual)):
        for j in range(len(individual)):
            cost += h[i][j] * d[individual[i]][individual[j]]
    return cost,

# 定义遗传算法
def ga(n, h, d):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("indices", random.sample, range(n), n)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", fitness, h=h, d=d)
    toolbox.register("mate", tools.cxPartialyMatched)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", np.mean)
    stats.register("Std", np.std)
    stats.register("Min", np.min)
    stats.register("Max", np.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, 
                                   stats=stats, halloffame=hof, verbose=True)
    return hof

# 读取数据并运行遗传算法


def genetic():
    print("task1:qap问题,遗传算法")
    data = read_data_from_folder('E:/project/2024/2024-buaa-kykt-intelligent-computing/qap/qap-problems')
    for n, h, d in data:
        best_solution = ga(n, h, d)
        print('Best solution:', best_solution)
genetic()