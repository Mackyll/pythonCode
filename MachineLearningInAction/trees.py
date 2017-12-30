from math import log
import operator


# 计算香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCount = {}
    for featvec in dataSet:
        currentLabel = featvec[-1]
        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCount:
        prob = float(labelCount[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def createDataSet():
    dataset = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataset, labels


# 数据划分
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        # 该行代码就是取数据集的第几行
        featList = [example[i] for example in dataSet]
        # 将数据放到一个集合里面，这里主要是为了得到唯一的数据
        uniqueVals = set(featList)
        newEntropy = 0.0
        # 这里计算信息增益，计算出来的信息增益越大久代表越好划分
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 构建的决策树是按照最大信息增益来构建的
# 首先找到最大信息增益的特征，然后按照特征划分之后，再从子集里面去查找最大信息增益的特征，再划分，以此类推
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    # 这里首先查找最大的信息增益的特征
    bestFeat = chooseBestFeatureToSplit(dataSet)
    # 找到最好特征集的label
    bestFeatLabel = labels[bestFeat]
    # 构建该label的一个子树
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    # 找到最好划分的所有值
    featValues = [example[bestFeat] for example in dataSet]
    # 找到该划分的唯一值
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        # 递归构建该子树的子集
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


if __name__ == '__main__':
    myDat, label = createDataSet()
    myTree = createTree(myDat, label)
    print(myTree)
