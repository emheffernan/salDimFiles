import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil
import random as rdm
import pandas as pd

oneNine = (1,9)
tmp = np.empty((1,4),('U',18))
data = np.empty((0,4),('U',18))
rowCount = 0

def getRand():
    a = rdm.choice(oneNine)
    b = rdm.choice(oneNine)
    c = rdm.choice(oneNine)
    d = rdm.choice(oneNine)
    letters = [a,b,c,d]
    return letters

#Change the dimensions specified in dims
def changeN(dims,img):
    for a in dims:
        if(img[a]==1):
           img[a]=9
        else:
            img[a]=1
    return

def writeLine(img1, img2, sameDiff, changedDim):
    tmp[0,0] = img1
    tmp[0,1] = img2
    tmp[0,2] = sameDiff
    tmp[0,3] = str(changedDim)
    return

#No change
for i in range(8):
    ind = getRand()
    fileOne = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
    while fileOne in data[:,0]: 
            ind = getRand()
            fileOne = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"

    writeLine(fileOne, fileOne, 's', -1)
    """ tmp[0,0] = fileOne
    tmp[0,1] = fileOne
    tmp[0,2] = 's'
    tmp[0,3] = '-1'"""
    data = np.vstack([data,tmp])
    rowCount += 1

#Change each dimension; get five random images per dimension 
for i in range(4):
    for j in range(8):
        ind = getRand()
        fileOne = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
        while fileOne in data[(8+i*8):rowCount,0] or fileOne in data[(8+i*8):rowCount,1]: 
            ind = getRand()
            fileOne = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
        dims = [i]
        changeN(dims, ind)
        fileTwo = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
        writeLine(fileOne, fileTwo, 'd', i)
        """ tmp[0,0] = fileOne
        tmp[0,1] = fileTwo
        tmp[0,2] = 'd'
        tmp[0,3] = str(i)"""
        data = np.vstack([data,tmp]) 
        rowCount += 1
#Change in two dimensions
#Dims 0+1
dimSet = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3],[0,1,2],[0,1,3],[0,2,3],[1,2,3],[0,1,2,3]]
for dims in dimSet:
    for i in range(2):
        ind = getRand()
        fileOne = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
        if(i==1): #Check for duplicates
            while fileOne==data[rowCount-1,0] or fileOne==data[rowCount-1,1]:
                ind = getRand()
                fileOne = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
        changeN(dims, ind)
        fileTwo = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
        writeLine(fileOne, fileTwo, 'd', dims)
        data = np.vstack([data,tmp]) 
        rowCount += 1
    
dirPath = os.getcwd()
updatedData = {'img1':data[:,0],'img2':data[:,1],'response':data[:,2],'dim':data[:,3]}
df = pd.DataFrame(updatedData)
df.to_csv(dirPath + '/Output/' + 'flowerParams.csv',index=False)


