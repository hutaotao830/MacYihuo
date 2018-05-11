# -*- coding: utf-8 -*-
import numpy as np

# N is input batch size; D_in is input dimension
# H is hidden dimension; D_out is output dimension
N, D_in, H, D_out = 64, 1000, 100, 10

# Create random input and output data
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

# Randomly initialize weights
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6
for t in range(10):
    h = x.dot(w1)
    h_relu = np.maximum(h, 0)

    y_pred = h_relu.dot(w2)





