from numpy import *
import operator
import matplotlib.pyplot as plt


# knn算法，intX是一个数据向量
def classify0(inX, dataSet, labels, k):
    # 首先计算向量与每个点的距离，然后从小到大排序
    dataSetSize = dataSet.shape[0]
    diffmat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffmat ** 2
    # 将矩阵的每一行向量相加
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    # argsort对参数进行排序，返回的是排序好的参数序号
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 找出前个点出现频率最高的类别
    for i in range(k):
        # 这里每一个数据点都有一个类型的参数，而且这些都是排序好的
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 从文件中将数据取出来，将类别和数据返回
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    fr.close()
    numberOfLines = len(arrayOLines)
    # zeros函数传入一个元组数据，初始化一个0矩阵
    returnmat = zeros((numberOfLines, 3))
    classlabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFormatLine = line.split("\t")
        returnmat[index, :] = listFormatLine[0:3]
        classlabelVector.append(int(listFormatLine[-1]))
        index += 1
    return returnmat, classlabelVector


# 将每一项数据归一化处理，因为每一类的数据大小不一样，直接相减的话会影响计算结果

def autoNorm(dataSet):
    # 计算所有列的最小值，不带参数是所有值的最小值,0代表所有列的最大值，1代表所有行的最大值
    minVals = dataSet.min(0)
    # 计算所有列的最大值
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    # shape函数是查看数据类型的维数，返回的是元组数据
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    # tile函数的意思是在行方向重复m次，列重复1次
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")
    normalMat, ranges, minVals = autoNorm(datingDataMat)
    m = normalMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normalMat[i, :], normalMat[numTestVecs:m, :],
                                     datingLabels[numTestVecs:m], 3)
        print("the classifier came back with:%d,the real answer is:%d "
              % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print("the total error rate is:%f" % (errorCount / float(numTestVecs)))


def classifyPerson():
    resultList = ["not at all", "in small does", "in large does"]
    persentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, persentTats, iceCream])
    classresult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print("you will probaly like this person:", resultList[classresult - 1])


if __name__ == "__main__":
    classifyPerson()
    # datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")
    # print(datingDataMat.argsort())
    # print(shape(datingLabels))
    # plt.figure()
    # s代表点点的尺寸，c代表点的颜色，这里每一个label对应一个点
    # plt.scatter(datingDataMat[:, 1], datingDataMat[:, 2], s=15.0 * array(datingLabels), c=15.0 * array(datingLabels))
    # plt.show()
