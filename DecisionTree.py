class DTreeNode:
    def __init__(self,p,index,value):
        self.featureIndex = index
        self.featureValue = value
        self.p = p
        self.left = None
        self.right = None

        print("Feature=",index+1,"value = ",value)

    def setLeft(self,node):
        self.left = node

    def setRight(self,node):
        self.right = node

def CalGini(sampleX,featureIndex,featureValue):
    D = len(sampleX)
    D1 = 0
    D2 = 0

    D11 = 0
    D21 = 0

    for x in sampleX:
        if (x[featureIndex] == featureValue):
            D1+=1
            if(x[4]==1):
                D11+=1
        else:
            D2+=1
            if(x[4]==1):
                D21+=1

    if(D1==0 or D2 ==0):
        return 0

    P1 = D11/D1
    P2 = D21/D2
    P =  (D1/D)*(2*P1*(1-P1))+(D2/D)*(2*P2*(1-P2))

    return  round(P,2)

def calMiniGini(sampleX,fList):
    minP = 1
    temP = 0
    minFeature = 0
    minValue = 0

    for key,feature in enumerate(fList):
        for value in feature[1:]:
            temP = CalGini(sampleX,feature[0],value)
            if(temP<minP):
                minP = temP
                minFeature = key
                minValue = value

    return (minP,minFeature,minValue)


def sepSample(sampleX,featureIndex,featureValue):
    list1 = []
    list2 = []

    for x  in sampleX:
        if(x[featureIndex]==featureValue):
            list1.append(x)
        else:
            list2.append(x)

    return (list1,list2)

def checkSample(sampleX):
    if(len(sampleX) == 1):
        return (0,sampleX[4])

    temp = sampleX[0][4]

    for x in sampleX[1:]:
        if(temp!=x[4]):
            return (1,0)

    return (0,sampleX[0][4])

def constructTree(sampleX,featurelist):
    result = calMiniGini(sampleX,featurelist)
    if(result[0] == 0):
        status = checkSample(sampleX)
        if(status[0]==0):
            return status[1]

    node = DTreeNode(result[0],result[1],result[2])
    newSample = sepSample(sampleX,result[1],result[2])
    del(featurelist[result[1]])
    node.setLeft(constructTree(newSample[0],featurelist))
    node.setRight(constructTree(newSample[1],featurelist))

    return node

sample = []
sample.append((1,2,2,1,2))
sample.append((1,2,2,2,2))
sample.append((1,1,2,2,1))
sample.append((1,1,1,1,1))
sample.append((1,2,2,1,2))
sample.append((2,2,2,1,2))
sample.append((2,2,2,2,2))
sample.append((2,1,1,2,1))
sample.append((2,2,1,3,1))
sample.append((2,2,1,3,1))
sample.append((3,2,1,3,1))
sample.append((3,2,1,2,1))
sample.append((3,1,2,2,1))
sample.append((3,1,2,3,1))
sample.append((3,2,2,1,2))

featurelist = []
featurelist.append((0,1,2,3))
featurelist.append((1,1,2))
featurelist.append((2,1,2))
featurelist.append((3,1,2,3))

constructTree(sample,featurelist)