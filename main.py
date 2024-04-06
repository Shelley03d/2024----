import sys
from qap import genetic

def task1():
    print("task1:qap问题")
    alg = int(input("请选择算法（1为遗传算法，2为粒子群算法，3为模拟退火算法）："))
    if alg == 1:
        genetic.genetic()
    elif alg == 2:
        print("粒子群算法")
    elif alg == 3:
        print("模拟退火算法")
    else:
        print("算法不存在")
        sys.exit(1)
def task2():
    print("task2：")

# 选择任务
task = int(input("input the task number: "))
if task == 1:
    task1()
elif task == 2:
    task2()
else:
    print("task not found")
    sys.exit(1)

# 运行
