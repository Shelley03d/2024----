import math
import numpy as np
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# 定义函数
def func(individual,which):
    cost = 0
    if which == 1:
        cost = func1(individual)
    elif which == 2:
        cost = func2(individual)
    else:
        print("Invalid function number")
        return
    return cost

# 定义梯度下降法
def gradient_descent(start, learn_rate, which, N, n_iter=50, tolerance=1e-06):
    vector = start.clone().detach().requires_grad_(True).to(device)
    vector.requires_grad = True
    for _ in range(n_iter):
        value = func(vector,which)
        value.backward()
        with torch.no_grad():
            diff = -learn_rate * vector.grad
            if torch.all(torch.abs(diff) <= tolerance):
                break
            vector += diff
            vector.grad.zero_()
    return vector

def func1(individual):
    cost = 0
    cost += torch.sum((individual-1)**2)
    for i in range(1,len(individual)):
        cost -= individual[i]*individual[i-1]
    return cost
    
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
    return cost

def gd(N,which):
    # 生成初始值
    if which == 1:
        BOUND_LOW, BOUND_UP = -N*N,N*N
    elif which == 2:
        BOUND_LOW, BOUND_UP = -600,600
    else:
        print("Invalid function number")
        return
    start = (BOUND_LOW + (BOUND_UP - BOUND_LOW) * torch.rand(N)).to(device)  # 这是初始点，随机生成
    
    # 设置学习率
    n_iter=50
    tolerance=1e-06
    learn_rate = 0.1  # 这是学习率
    # 使用梯度下降法找到函数的最小值
    minimum = gradient_descent(start, learn_rate,which,N)
    print('极小值取于: ', minimum.data)
    print('极小值是: ', func(minimum,which).data)
    return minimum.data,func(minimum,which).data

out = gd(10,1)
for i in range(125):
    tmp = gd(10,1)
    if(tmp[1]<out[1]):
        out = tmp
print('最小值取于: ', out[0])
print('最小值：' , out[1])