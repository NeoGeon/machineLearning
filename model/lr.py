import numpy as np
import math

class lr:
    def __init__(self, feature, label):
        self.feature = feature
        self.nx, self.ny = feature.shape
        self.label = label
        self.weights = np.random.rand(self.nx)
        self.bias = 0
        

    def activate(self,x):
        return 1/(1+exp(-x))
 
    def loss(self, target, t):
        return (target-t)**2
        
    def train(self, epoch=100, lr=0.01):
        for i in range(epoch):
            partial_weights = np.random.rand(self.nx)
            for feature, label in (self.feature, self.label):
                        
            self.weights += lr*patial_weights
            if i%20 == 1:
               lr /= 2

    def predict(self, x):
        return self.weights*self.feature + self.bias

    def classify(self,x):
        return self.activate(self.weights*self.feature + self.bias)
