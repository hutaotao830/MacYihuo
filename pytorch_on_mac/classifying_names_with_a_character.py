# coding = utf-8
# user   = hu_yang_jie
import os
import time

from io import open
import glob
import unicodedata
import string
import torch
import torch.nn as nn

data_root = '/Users/huyangjie/Desktop/dataset/data/names/'


def findFile(path): return glob.glob(path+'*.txt')


# print(findFile(data_root))
all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)


# Turn a Unicode string to plain ASCII.
def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )


print(unicodeToAscii('Ślusàrski'))

# Build the category_lines dictionary, a list of names per language
# category 种类分类
category_lines = {}
all_categories = []


def readLines(filename):
    lines = open(filename, encoding='utf-8').read().strip().split('\n')
    return [unicodeToAscii(line) for line in lines]


for filename in findFile(data_root):
    category = filename.split('/')[-1].split('.')[0]
    # print(category)
    all_categories.append(category)
    lines = readLines(filename)
    category_lines[category] = lines

n_categories = len(all_categories)
print('all_categories num is:', n_categories)


# Find letter index from all_letters, e.g. "a" = 0
# letter: 单个字母 index: 索引
def letterToIndex(letter):
    return all_letters.find(letter)


# Just for demonstration, turn a letter into a < 1 x n_letters> Tensor
def letterToTensor(letter):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letterToIndex(letter)] = 1
    return tensor


# Turn a line into a <line_length x 1 x n_letters>
# or an array of one-hot letter vectors
def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)] = 1
    return tensor


print(lineToTensor('hu_yang_jie').size())


###########################################
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()

        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return(torch.zeros(1, self.hidden_size))


n_hidden = 128
rnn = RNN(n_letters, n_hidden, n_categories)
print(rnn)

input = lineToTensor('huyangjie')
print('input is: /n', input)
hidden = torch.zeros(1, n_hidden)
output, next_hidden = rnn(input[0], hidden)
print(output)
if __name__ == '__main__':
    pass
