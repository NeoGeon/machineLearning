#!/usr/bin/python
import numpy as *

class DecisionTree:
    def __init__(self, yipsilon, feature={}, data, label):
        self.yipsilon = yipsilon
        self.feature = feature
        self.isLeaf = True
        self.index = 0
        self.value = []
        self.child = []
        self.data = data
        self.label = label
        self.myClass = None
   
    def classify(self, x):
        if self.isLeaf:
            return self.myClass
        else:
            i = 0
            for v in self.value:
                i = i + 1
                if v > x[self.index]:
                    return self.child[i]
            return self.child[-1]
    
    def train():
        self.isLeaf = False
        maxInfoGain = 0
        maxIndex = 0
        x, y = shape(self.data)
        HD = Entropy(self.data, self.label)
        for i in range(x):
            if i not in feature:
                HCD = HD - CondionalEntropy(self.data, self.label, i)
                if maxInfoGain > HCD
                    maxInfoGain = HCD
                    maxIndex = i
        if yipsilon > maxInfoGain:
            classes = {}
            for item in label:
                classes[item] + = 1
            self.IsLeaf = True
            self.myClass = max(classes) #!
        else:
            self.featrue[i] = 1
            dataSets = []
            labelSets = []
            for (itemD, itemL) in zip(self.data, self.lable): # pivot not implemented!!!
                dataSets
                
            for (dt, lt) in (dataSets, labelSets):
                subTree = DecisionTree(self.yipsilon, self.feature, dt, lt)
                subTree.train()
                self.child.apppend(subTree)
            
           

def Entropy(data, label):
    x,y = shape(data)
    classDict = {}
    for item in label:
        classDict[item] = classDict[item]+1
    entropy = 0.
    for item in classDict:
        entropy = classDict[item]/x*log(classDict[item]/x)
    return entropy

def ConditionalEntropy(data, label, featureIndex):
    x, y = shape(data)
    subSetData = {}
    subSetLabel = {}
    zipData = zip(data, label)
    for (item, class_) in zipData:
        if item[featureIndex] not in subSetData:
            subSetData[item[featureIndex]] = []
            subSetLable[item[featureIndex]] = []
        subSetData[item[featureIndex]].append(item)
        subSetLabel[item[featureIndex]].append(class_)
    entropy = 0.
    for name in subSetData:
        entropy += len(subSetData[name])/x*Entropy(subSetData[name], subSetLabel[name])
    return entropy
        
        


    
