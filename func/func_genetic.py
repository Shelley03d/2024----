from deap import base, creator, tools, algorithms
import random
import numpy as np
import math
# 这是你的函数，我假设它接受一个列表作为输入
def func(individual,which=1):
    cost = 0
    if which == 1:
        cost = func1(individual)
    elif which == 2:
        cost = func2(individual)
    else:
        print("Invalid function number")
        return
    return cost

def ga(N,which=1):
    # 创建一个最小化问题
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()

    # 初始化
    #  N:函数的变量数量
    if which == 1:
        # 为每个变量注册一个随机生成的函数
        BOUND_LOW, BOUND_UP = -N*N,N*N
    elif which == 2:
        BOUND_LOW, BOUND_UP = -600,600
    else:
        print("Invalid function number")
        return

    toolbox.register("attr_float", random.uniform, BOUND_LOW, BOUND_UP)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=N)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # 适应度函数
    toolbox.register("evaluate", func,which=which)

    # 交叉，突变和选择操作
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # 初始化种群
    pop = toolbox.population(n=50)

    # 运行遗传算法
    result = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, verbose=False)

    # 打印最优解
    best_individual = tools.selBest(pop, 1)[0]
    print('Best individual is %s, %s' % (best_individual, best_individual.fitness.values))

def func1(individual):
    cost = 0
    cost += sum((np.array(individual)-1)**2)
    for i in range(1,len(individual)):
        cost -= individual[i]*individual[i-1]
    return cost,
    
def func2(individual):
    cost = 0
    for i in range(len(individual)):
        cost += (individual[i]**2)
    cost /= 4000
    minus = 1
    for i in range(len(individual)):
        minus *= math.cos(individual[i]/math.sqrt(i+1))
    cost -= minus
    cost += 1
    return cost,

ga(10,2)