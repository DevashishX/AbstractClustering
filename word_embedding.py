from gensim.models import KeyedVectors
from gensim.models.wrappers import FastText
import numpy as np

class Word2Vec(object):
    """docstring for Word2Vec."""

    def __init__(self):
        # add testing code here
        print("Loading Model")
        self.model = KeyedVectors.load_word2vec_format("enter filename here")
        print("Done! Model Loaded. Vector Size is "+len(model["hello"]))


    def get_embeddings(self, words):
        return [self.model[x] for x in words if x in self.model]



class GloveVectors(object):
    """docstring for GloveVectors."""

    def __init__(self, filename):
        print("Loading Model")
        self.model = self.loadGloveModel(filename)


    def loadGloveModel(self, gloveFile):
        f = open(gloveFile,'r')
        model = {}
        for line in f:
            splitLine = line.split()
            word = splitLine[0]
            embedding = np.array([float(val) for val in splitLine[1:]])
            model[word] = embedding
        print("Done! Model Loaded. Vector Size is "+str(len(model["hello"])))

        f.close()
        return model

    def get_embeddings(self, words):
        # return [self.model[x] for x in words]
        return [self.model[x] for x in words if x in self.model]



class FastTextVectors(object):
    """docstring for FastTextVectors."""

    def __init__(self):
        # add testing code here
        print("Loading Model")
        self.model = FastText.load_fasttext_format("enter filename here")
        print("Done! Model Loaded. Vector Size is "+len(model["hello"]))

    def get_embeddings(self, words):
        # return [self.model[x] for x in words]
        return [self.model[x] for x in words if x in self.model]
        
