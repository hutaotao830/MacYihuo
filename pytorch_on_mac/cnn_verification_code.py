# coding = utf-8
# user   = hu_yang_jie

import os
import time
import torch
import torch.nn as nn
import cv2 as cv
import numpy as np
import torch.nn.functional as F
import torch.nn as nn
from verification_code_pytorch import gene_code
from torch.utils.data import dataloader, dataset
from torchvision import transforms
from warpctc_pytorch import CTCLoss
from torch.autograd import Variable


real_code_path = '/Users/huyangjie/Desktop/code.png'

transform1 = transforms.Compose(
    [transforms.ToTensor()
     ]
)
class MyLstm(nn.Module):
    def __init__(self):
        super(MyLstm, self).__init__()
        self.out_list = []
        self.rnn = nn.LSTM(
            input_size=30,
            hidden_size=128,
            num_layers=1,
            batch_first=True
        )
        self.out = nn.Linear(128, 36)

    def forward(self, x):
        r_out, (h_n, h_c) = self.rnn(x, None)
        # print(r_out.size())
        out = self.out(r_out)
        return out
lstm = MyLstm()
print(lstm)


def create(batch_num):
    """
    Create batch of verification code
    batch_num: batch
    :return:
    """
    code_list = []
    for i in range(1, batch_num+1):
        code_list.append([next(gene_code())])
    return code_list


# # Real verification_code img(from taobao)
# img2 = cv.imread(real_code_path, 0)
# np.set_printoptions(threshold=np.nan, linewidth=10000)
# print(img2/255)
# print('*'*500)
##############################################################
# # create verification_code from verification_code_pytorch.py
# img, text = next(gene_code())
# img_cv = cv.cvtColor(np.asarray(img), cv.COLOR_RGBA2GRAY)
# print((img_cv-1)/255)
# img_tensor = torch.tensor(img_cv)
# print(img_tensor)
np.set_printoptions(threshold=np.nan, linewidth=10000)
torch.set_printoptions(threshold=10000, linewidth=10000)
ctc_loss = CTCLoss()
for batch in range(10):
    img, label = next(gene_code())
    img_cv = cv.cvtColor(np.asarray(img), cv.COLOR_RGBA2GRAY)-1
    img_tensor = torch.tensor(img_cv, dtype=torch.float)/255.0
    # img_tensor = torch.tensor(img_cv)/255
    x = torch.t(img_tensor)
    x = x.view(1, 100, 30)

    out = lstm(x)
    print(out.size())
    print(out)
    l = Variable(torch.IntTensor([1, 2, 3, 4]))
    l_s = Variable(torch.IntTensor([4]))
    x_s = Variable(torch.IntTensor([100]))
    print(l)
    print(l_s)
    print(x_s)
    cost = ctc_loss(out, l, l_s, x_s)
    print(out.size())
    # print(img_tensor)
    # print(torch.t(img_tensor))
    # break
if __name__ == '__main__':
    pass
