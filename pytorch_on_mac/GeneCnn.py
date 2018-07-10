# -*- coding: utf-8 -*-
"""
Created on Wed May 30 19:51:21 2018

@author: hubinbin
"""
import sys
sys.path.append("..") 

from GeneData import GeneDataset
from GeneData import GeneDataset_test

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

batch_size = 128

train_data = GeneDataset()
test_data = GeneDataset_test()

train_loader = DataLoader(train_data,batch_size=batch_size,shuffle=True)
test_loader=DataLoader(test_data,batch_size=64,shuffle=False)

class MyCnn(nn.Module):
    def __init__(self):
        super(MyCnn, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 16, 3, 1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(16, 32, 3, 1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.out = nn.Linear(4416, 36)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output

model = MyCnn()
#print(model)

optimizer = torch.optim.Adam(model.parameters(),lr=0.001)
loss_func = torch.nn.MultiLabelMarginLoss()

epoch=0
while(1):
    print('epoch {}'.format(epoch + 1))
    # training-----------------------------
    model.train()
    train_loss = 0.
    train_acc = 0.
    for batch_x, batch_y in train_loader:
        out = model(batch_x)
        loss = loss_func(out, batch_y)
        train_loss += loss.item()
        
        sor, ind = torch.sort(out, descending=True)
        pred,_ =torch.sort(ind[:,:4], descending=True)
        lable_rel,_ =torch.sort(batch_y[:,:4], descending=True)
        train_correct = (pred == lable_rel).sum()
        train_acc += train_correct.item()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print('Train Loss: {:.6f}, Acc: {:.6f}'.format(train_loss / (len(
        train_data)), train_acc / (len(train_data))))

    # evaluation--------------------------------
    model.eval()
    eval_loss = 0.
    eval_acc = 0.
    for batch_x, batch_y in test_loader:
        with torch.no_grad():
            out = model(batch_x)
            loss = loss_func(out, batch_y)
            eval_loss += loss.item()
            
            sor, ind = torch.sort(out, descending=True)
            pred,_ =torch.sort(ind[:,:4], descending=True)
            lable_rel,_ =torch.sort(batch_y[:,:4], descending=True)
            num_correct = (pred == lable_rel).sum()
            eval_acc += num_correct.item()
    print('Test Loss: {:.6f}, Acc: {:.6f}'.format(eval_loss / (len(
        test_data)), eval_acc / (len(test_data))))
    
    if (train_acc / (len(train_data)))>0.99:
        break
    epoch+=1
    
torch.save(model, 'GeneCnn.pthx')    
#torch.save(model.state_dict(),'TrobotCnn.pth')

