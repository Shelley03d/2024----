# 2024-科研课堂代码
文件树如下：
│  main.py
│  model.pth
│  README.md
│ 
│  
├─func
│      func_fnn.py
│      func_gd.py
│      func_genetic.py
│      
└─qap
    │  genetic.py
    │  qap_pso.py
    │  qap_sa.py
    │  
    ├─qap-problems
    │      QAP12.dat
    │      QAP21.dat
    │      QAP25.dat
    │      QAP30.dat
    │      QAP32.dat
    │      
    └─__pycache__
            genetic.cpython-311.pyc

## qap文件夹是工厂二次分配问题

- genetic.py是遗传算法
- qap_pso.py是粒子群算法
-  qap_sa.py是模拟退火算法

## func文件夹是函数优化问题

-  gd是梯度下降算法
- genetic是遗传算法



注：

main.py是启动器，在施工

qap-problems文件内存储了qap问题的数据集

 func_fnn.py 是一个神经网络算法，还有一点点细节 在施工

model.pth 是对应的训练权重

