#!/usr/bin/python3
import pandas as pd
import numpy as np
        

class Iris:
    def __init__(self, fileName='./iris.data'):
        self.fileName = fileName
        self.Dataframe = pd.read_csv(self.fileName)
        self.data = self.Dataframe.values
        self.train_data = self.data[:,0:4]
        self.label_data = self.data[:,4]
        self.label_num = {}
        self.label_dataN = self.labelToNum()
        self.total = len(self.label_data)

    def features(self):
        return self.train_data

    def labels(self):
        return self.label_data

    def labelToNum(self):
        index = 0
        ret = []
        for label in self.label_data:
            if not label in self.label_num:
               self.label_num[label] = index
               index = index + 1
        for label in self.label_data:
            ret.append(self.label_num[label])
        return ret
    
    def labelNum(self):
        return self.label_dataN
    
    def shuffle(self):
        return self.Dataframe.sample(frac=1)    

    def train_test_split(self, frac):
        newFrame = self.shuffle()
        test_set = []
        train_set = []
        train_total = self.total - int(frac*self.total)
        train_set = newFrame.values[:train_total,:]
        test_set = newFrame.values[train_total:,:]
        return train_set, test_set
       
class Preprocess:  # only deal with numpy
    def __init__(self, data):
        self.data = data
        self.nx, self.ny = self.data.shape

    def num(self, columns):
        index = 0
        check = {}
        for i,label in enumerate(self.data[:,columns]):
            if not label in check:
                check[label] = index
                index = index + 1
            self.data[i, columns]=check[label]
             
    def norm(self, columns):
        s = sum(item for item in self.data[:, columns])
        maxN = max(item for item in self.data[:, columns])
        minN = min(item for item in self.data[:, columns])
        mean = s/self.nx
        if s != 0 and maxN != minN:
           for i , item in enumerate(self.data[:, columns]):
               self.data[i, columns] = (item - mean)/(maxN-minN)
           

    def feature_label_split(self):
        return self.data[:,:self.ny-1], self.data[:,self.ny-1]

if __name__ == "__main__":
    dataset = Iris()
    train_set, test_set =  dataset.train_test_split(0.1)
    train_set = Preprocess(train_set)
    train_set.num(4)
    for i in range(4):
        train_set.norm(i)
    data, label  = train_set.feature_label_split()
    print(data)
