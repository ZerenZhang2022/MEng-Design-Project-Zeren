# !/usr/bin/python3
# -*- coding:utf-8 -*-


import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


'''--------AlexNet structure--------'''
class AlexNet(nn.Module):
    def __init__(self, width_mult=1):
        super(AlexNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2, stride=2),  
            nn.ReLU(inplace=True),
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.ReLU(inplace=True),
        )

        self.layer3 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
        )

        self.layer4 = nn.Sequential(
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
        )
        self.layer5 = nn.Sequential(
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.ReLU(inplace=True),
        )

        self.fc1 = nn.Linear(256 * 3 * 3, 1024)
        self.fc2 = nn.Linear(1024, 512)
        self.fc3 = nn.Linear(512, 10) #10 outputs

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        # print(x.shape)
        x = x.view(-1, 256 * 3 * 3)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)

        return x


'''--------Training--------'''
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

epochs = 500
batch_size = 8192
lr = 0.01

transform = transforms.Compose([
    transforms.Resize([32,32]),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    # transforms.Normalize(mean=[.5,.5,.5],std=[.5,.5,.5]),
    ])

train_dataset = torchvision.datasets.CIFAR10(
    root= './data', train = True,
    download =True, transform = transform)
train_loader = DataLoader(train_dataset,
                          batch_size=batch_size,
                          shuffle = True,)
net = AlexNet().cuda(device)
loss_func = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(),lr=lr,momentum=0.9)

train_loss = []
for epoch in range(epochs):
    sum_loss = 0
    for batch_idx,(x,y) in enumerate(train_loader):
        x = x.to(device)
        y = y.to(device)
        pred = net(x)

        optimizer.zero_grad()
        loss = loss_func(pred,y)
        loss.backward()
        optimizer.step()
        sum_loss += loss.item()
        train_loss.append(loss.item())
        if (batch_idx)%5==0: print(["epoch:%d , batch:%d , loss:%.3f" %(epoch,batch_idx,loss.item())])
    if (epoch+1)%5==0: torch.save(net.state_dict(), r'/content/drive/MyDrive/ECE6930/Alexnet-0201-01/'+ 'Alexnet-Cifar10-epoch%d.h5' %(epoch+1))

