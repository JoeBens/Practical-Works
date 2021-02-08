import numpy as np
import pickle
import pydot
import itertools
import matplotlib.pyplot as plt

from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier as DTree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.model_selection import ShuffleSplit
from sklearn import datasets
from sklearn import svm

##### ENTROPIE ######

def entropie(vect):
    size = len(vect)
    unique, countUnique = np.unique(vect,return_counts=True)
    p = countUnique/size
    return -np.sum(p*np.log(p))

def entropie_cond(list_vect):
    totalLen = np.sum([len(list_vect[i]) for i in range(list_vect.shape[0])])
    ans = np.sum([len(vect) * entropie(vect) for vect in list_vect])
    return ans/totalLen

# data : tableau ( films , features ) , id2titles : dictionnaire id -> titre ,
# fields : id feature -> nom
[data, id2titles, fields] = pickle.load(open(".\imdb_extrait.pkl","rb"))

datax = data[:,:32]
datay = np.array([1 if x [33] >6.5 else -1 for x in data ])

def getbothEntrop(datax, datay, nbBinAttrib = 28):

    #init both array
    AttribBinEntrop = np.zeros(nbBinAttrib)
    AttribBinEntropCond = np.zeros(nbBinAttrib)

    #i is the field we want to get the entropy of
    for i in range(0,len(AttribBinEntrop)):

        #get entropy for the whole field i
        AttribBinEntrop[i] = entropie(datax[:,i])

        #get the entropy of the field i conditionel to the datay array
        #since the partion is binary (0,1) the is a split of a n=2 partitions
        AttribBinEntropCond[i] = entropie_cond(np.array([datay[datax[:,i] == 1], datay[datax[:,i] != 1]]))
    
    return AttribBinEntrop,AttribBinEntropCond

# enty = entropie(datay)
ent,entCond = getbothEntrop(datax,datay,32)

# todo do stuff with mathplot lib to show the difference between 

# print(entCond-ent)
# print("best attribut partition is " + fields[np.argmax(enty-entCond)]) 

####### TREE #######



#this loop show us the deeper the tree the better the score is
#this is normal because we split the data with a wider range the deeper we go
#
#there is also something to concider, we test and train the same data, ench the
#good performance, but we have to take that in concideration. and we can totally relate
#to the ouputed score

def treeClassifTesting(datax, datay, maxDepth=29,graphical=False):
    scores = []
    for i in range(1,maxDepth):
        dt = DTree()
        dt.max_depth = i # on fixe la taille max de l ’ arbre a i
        dt.min_samples_split = 2 # nombre minimum d ’ exemples pour spliter un noeud

        #train data
        dt.fit(datax,datay)

        #test data
        dt.predict(datax[:200 ,:])

        #different method to display the result
        if(not graphical):
            print("max depth of " + str(i) + " with score of " + str(dt.score(datax,datay)))
        else:
            scores.append(dt.score(datax,datay))

    if(graphical):
        #we plot the curve of the data
        plt.plot(scores)
        plt.show()

# sinon utiliser http://www.webgraphviz.com/ par exemple ou https://dreampuf.github.io/GraphvizOnline
# export_graphviz(dt , out_file ="tree.dot", feature_names = dict(itertools.islice(fields.items(), 32)))


######### Sous et sur apprentisage #########

#same loop as the testClassifTesting function but there is a parameter trainsize wich split the
#data in proportion to this parameter
#
#since we perfome the training and the testing on different dataset the score are lower BUT
#more reliable than before, netherless we can see a flaw, we only use the same "range" of data
#for testing and training. One option is to shuffle the data and another one it to use cross validation

def treeClassifDiff(datax, datay, trainSize=0.8, maxDepth=29):
    xTrain, xTest, yTrain, yTest =  train_test_split(datax,datay,train_size=trainSize)
    scoresTr = []
    scoresTe = []
    for i in range(1,maxDepth):
        dt = DTree()
        dt.max_depth = i # on fixe la taille max de l ’ arbre a i
        dt.min_samples_split = 2 # nombre minimum d ’ exemples pour spliter un noeud

        #train data
        dt.fit(xTrain,yTrain)

        #test data
        dt.predict(xTest)
        
        #perform a score on both the training data and the test data
        scoresTr.append(dt.score(xTrain,yTrain))
        scoresTe.append(dt.score(xTest,yTest))
    
    return scoresTr,scoresTe

# aTr,aTe = treeClassifDiff(datax,datay,0.2)
# bTr,bTe = treeClassifDiff(datax,datay,0.8)
# cTr,cTe = treeClassifDiff(datax,datay,0.5)

# plt.plot(aTr, label="train: 0.2")
# plt.plot(aTe, label="test: 0.8")
# plt.plot(bTr, label="train: 0.8")
# plt.plot(bTe, label="test: 0.2")
# plt.plot(cTr, label="train: 0.5")
# plt.plot(cTe, label="test: 0.5")
# plt.legend()
# plt.show()

######### Cross validation #########


def treeClassifCrossVal(datax, datay, trainSize=0.8,nbSplit=5, maxDepth=29):
    scoresTr = []
    scoresTe = []
    for i in range(1,maxDepth):
        dt = DTree()
        dt.max_depth = i # on fixe la taille max de l ’ arbre a i
        dt.min_samples_split = 2 # nombre minimum d ’ exemples pour spliter un noeud

        cv = ShuffleSplit(n_splits=5,test_size=0.2)

        scores = cross_validate(dt, datax, datay,cv=cv, scoring='f1', return_train_score=True)
        
        #perform a score on both the training data and the test data
        scoresTr.append(scores['train_score'].mean())
        scoresTe.append(scores['test_score'].mean())
    
    return scoresTr,scoresTe


# aTr,aTe = treeClassifCrossVal(datax,datay)
# plt.plot(aTr, label="train")
# plt.plot(aTe, label="test")
# plt.legend()
# plt.show()
