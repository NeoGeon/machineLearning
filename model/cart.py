#!/usr/bin/python
import numpy as np

class CART:
    def __init__(self,data, gini=0.000001):
        self.left = None
        self.right = None
        self.featureIndex = -1
        self.splitValue = 0
        self.data = data
        self.isLeaf = True
        #print(np.shape(data))
        self.x, self.y = np.shape(data)
        self.label = max(self.data[:,self.y-1])
        self.gini = gini
        #print('init')
        
    def train(self):
        self.isLeaf=False
        classLine = [item for item in self.data[:,self.y-1] ]
        #print(self.giniEstimater(classLine))
        if self.giniEstimater(classLine)>self.gini and self.x>2:
            self.isLeaf=False
            data1,data2 = self.featureChooseAndSplit(self.data)
            #print(type(data1))
            self.left = CART(data1)
            #print(np.shape(data1))
            #print(np.shape(data2))
            self.right = CART(data2)
            self.left.train()
            self.right.train()
        else:
            self.label = max(classLine)
            self.isLeaf = True
            

    def featureChooseAndSplit(self,data):
        bestGini = 1.0
        bestFeature = 0
        featureList = [i for i in range(self.y)]
        for feature in featureList[:-1]:
            featureSet = data[:,feature]
            featureSorted=sorted(set(featureSet))
            for item in featureSorted[:-1]:
                data1 = [data[i,self.y-1] for i, elem in zip(range(self.x), featureSet) if elem <=item]
                data2 = [data[i,self.y-1] for i, elem in zip(range(self.x), featureSet) if elem >item]
                gini = float(self.giniEstimater(data1)*len(data1))/float(self.x) + \
                       float(self.giniEstimater(data2)*len(data2))/float(self.x)
                if gini<bestGini:
                    bestGini=gini
                    self.featureIndex = feature
                    self.splitValue = item
        #print(bestGini)
        data1 = [dataLine for dataLine in data if dataLine[self.featureIndex] <= self.splitValue ]
        data2 = [dataLine for dataLine in data if dataLine[self.featureIndex] > self.splitValue ]
        return np.array(data1), np.array(data2)

    def giniEstimater(self,dataSet):
        length = len(dataSet)
        countDict = {}
        for item in dataSet:
            if item not in countDict:
                countDict[item]=1
            else:
                countDict[item]+=1
        gini=0
        for cnt in countDict.values():
            gini+=pow(cnt/float(length),2)
        gini=1-gini
        return gini
        
    def predict(self,x):
         if self.isLeaf:
             return self.label
         else:
             #print('predict', self.featureIndex, len(x))
             if x[self.featureIndex]<=self.splitValue:
                 return self.left.predict(x)
             else:
                 return self.right.predict(x)

    def printT(self,space=' '):
        if not self.isLeaf:
            print(space,self.splitValue, self.featureIndex)   
            space+=space     
            self.left.printT(space=space)
            self.right.printT(space=space)
        else:
            print(space, self.label)

if __name__=='__main__':
    data = []
    with open('data.test','r') as fd:
        for sline in fd:
            sline = sline[1:len(sline)-2]
            #print(sline)
            line =[float(s) for s in sline.split(',')]
            data.append(line)
    print(len(data))
    print(np.shape(np.array(data)))
    cart = CART(np.array(data))
   
    cart.train()
    cart.printT()
    data=[]
    with open('testData.test','r') as fd:
        for sline in fd:
            sline = sline[1:len(sline)-2] 
            line = [float(s) for s in sline.split(',')]
            data.append(line)
    total = len(data)
    cnt = 0 
    for line in data:
        #print(cart.predict(line[:-1]),line[-1])
        if cart.predict(line[:-1])==line[-1]:
            cnt += 1
    print('precision:',cnt/total, cnt, total)
   
