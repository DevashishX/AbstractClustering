import numpy as np
import pandas as pd
import re

def loadGloveModel(gloveFile):
    f = open(gloveFile,'r')
    model = []
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        # embedding = np.array([float(val) for val in splitLine[1:]])
        model.append(word)
    print("Done.",len(model)," words loaded!")
    f.close()
    return model

def writeinto(model, filename):
    f = open(filename, "w")
    model = model[int(len(model)*2/3):int(len(model)*1/3)]
    for i in model:
        f.write(i)
        f.write("\n")
    f.close()


m = loadGloveModel("glove.6B.50d.txt")
writeinto(m, "glove.one3rd.names.txt")