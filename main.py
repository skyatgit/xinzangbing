import numpy as np
import torch
import torch.nn as nn
data=np.loadtxt('heart.csv',float,delimiter=',')#加载数据
data=torch.tensor(data).float()#转换成张量数据
data=(data-data.min(0).values)/(data.max(0).values-data.min(0).values)#归一化处理

train_data,test_data=data.split([212,91],dim=0)#拆分成训练数据和测试数据
train_x,train_y=train_data.split([13,1],dim=1)#拆分成训练数据和正确数据
test_x,test_y=test_data.split([13,1],dim=1)#拆分成测试数据和正确数据
#搭建一个13输入1输出的神经网络
myNet = nn.Sequential(
    nn.Linear(13, 1),
    nn.Sigmoid()
)

optimzer = torch.optim.SGD(myNet.parameters(), lr=0.001,momentum=0.9)#设置优化器
loss_func = nn.BCELoss()#设置损失函数
for epoch in range(100000):
    out = myNet(train_x)#对训练数据进行预测
    loss = loss_func(out, train_y)#计算损失
    if epoch%10000==0:
        test_out = myNet(test_x)#对测试数据进行预测
        test_loss = loss_func(test_out, test_y)#计算损失

        mask_train = out.ge(0.5).float()#判断是否患病
        count_train = (mask_train == train_y).sum()  # 计算正确预测的样本个数
        acc_train = count_train.item() / train_x.size(0)  # 计算精度

        mask_test = test_out.ge(0.5).float()#判断是否患病
        count_test = (mask_test == test_y).sum()  # 计算正确预测的样本个数
        acc_test = count_test.item() / test_x.size(0)  # 计算精度

        print(epoch,':',acc_train,'--',loss,'----',acc_test,'--',test_loss)
    optimzer.zero_grad()  # 清除梯度
    loss.backward()#反向传播
    optimzer.step()#优化
print(myNet(train_x))
print(myNet(test_x))