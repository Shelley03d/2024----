import torch
import torch.nn as nn
import torch.optim as optim

# 创建设备对象
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def func1(x):
    output = 0
    output += torch.sum((x-1)**2)
    return output

def func2(x):
    output = 0
    output += torch.sum(x**2)
    return output

# 定义神经网络模型
def fun_fnn(N,which):
    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.fc1 = nn.Linear(N, 64)  #  N是变量数量
            self.fc2 = nn.Linear(64, 64)
            self.fc3 = nn.Linear(64, 1)

        def forward(self, x):
            x = torch.relu(self.fc1(x))
            x = torch.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    # 初始化模型和优化器
    model = Net().to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    # 训练模型
    for i in range(1000):  # 这是迭代次数
        optimizer.zero_grad()
        inputs = torch.randn(N).to(device)  # 这是输入数据
        
        
        outputs = model(inputs)
        criterion = nn.MSELoss()
        if(which == 1):
            loss = criterion(outputs, func1(inputs))
        elif(which == 2):
            loss = criterion(outputs, func2(inputs))
        loss.backward() #反向传播
        optimizer.step()

    # 使用训练好的模型预测新的数据
    inputs = torch.randn(N).to(device)  # 这是新的输入数据
    outputs = model(inputs)
    print('The minimum value of the function is:', outputs.item())
    
fun_fnn(10,1)  # 10是变量数量，1是函数编号