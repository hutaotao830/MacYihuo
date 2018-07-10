# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 18:37:11 2018

@author: hubinbin
"""

from torch.utils.data import Dataset
from verification_code_pytorch import gene_code
import cv2 as cv
import numpy as np
import torch

Train_Size=10000
Test_Size=1000

class GeneDataset(Dataset):
    """ Trobot dataset."""

    # Initialize your data, download, etc.
    def __init__(self):
        code_list = []
        for i in range(1, Train_Size+1):
            code_list.append((next(gene_code())))
        self.code_list=code_list
        self.len = len(self.code_list)

    def __getitem__(self, index):        
        img, label = self.code_list[index]
        img_cv = cv.cvtColor(np.asarray(img), cv.COLOR_BGR2GRAY)
        img_tensor = torch.tensor(img_cv, dtype=torch.float)/255.0
        img_tensor = img_tensor.view(1, 30, 100)
        label_tensor = torch.tensor(label)
        
        return img_tensor, label_tensor

    def __len__(self):
        return self.len
    
class GeneDataset_test(Dataset):
    """ Trobot dataset."""

    # Initialize your data, download, etc.
    def __init__(self):
        code_list = []
        for i in range(1, Test_Size+1):
            code_list.append((next(gene_code())))
        self.code_list=code_list
        self.len = len(self.code_list)

    def __getitem__(self, index):        
        img, label = self.code_list[index]
        img_cv = cv.cvtColor(np.asarray(img), cv.COLOR_BGR2GRAY)
        img_tensor = torch.tensor(img_cv, dtype=torch.float)/255.0
        img_tensor = img_tensor.view(1, 30, 100)
        label_tensor = torch.tensor(label)
        
        return img_tensor, label_tensor

    def __len__(self):
        return self.len