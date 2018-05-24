# coding = utf-8
# user   = hu_yang_jie

import torch
from torch.autograd import Variable
from warpctc_pytorch import CTCLoss
ctc_loss = CTCLoss()
# expected shape of seqLength x batchSize x alphabet_size
probs = torch.FloatTensor([[[0.1, 0.6, 0.1, 0.1, 0.1], [0.1, 0.1, 0.6, 0.1, 0.1]]]).transpose(0, 1).contiguous()
print(probs)
print(probs.size())
print('*' * 100)

labels = Variable(torch.IntTensor([1, 2]))
print(labels)
print('*' * 100)

label_sizes = Variable(torch.IntTensor([2]))
print(label_sizes)
print('*' * 100)

probs_sizes = Variable(torch.IntTensor([2]))
print(probs_sizes)
print('*' * 100)

probs = Variable(probs, requires_grad=True) # tells autograd to compute gradients for probs

# probs.no_grad()

cost = ctc_loss(probs, labels, probs_sizes, label_sizes)
print(cost)
cost.backward()
cost.backward()
