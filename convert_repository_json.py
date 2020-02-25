import json
import numpy as np
import pandas as pd
from pprint import pprint
from preprocessing import AbstractPreprocessor, preproc
import os

def simpleSplit(text):
    return text.split()

#reads joson form the repo files. Every line is a valid json but the whole doc is not
def repo_read_json(filename, lemma = True):
    with open(filename, "r") as fd:
        line = fd.readline()
        while line != "":
            if line.find("bibo:abstract") != -1:
                jsonobj = json.loads(line)
                # print(jsonobj)
                id = jsonobj["identifier"]
                pretitle = jsonobj["bibo:shortTitle"]
                title = preproc(pretitle, to_lemmatize=lemma)
                abstract = jsonobj["bibo:abstract"]
                
                # print(str(id) + "Type of id: " + str(type(id)))
                # print(title + "Type of title: " + str(type(title)))
                # print(abstract + "Type of abstract: " + str(type(abstract)))
                print(id, pretitle, title, abstract, sep="\n")
            line = fd.readline()
            
class AbstractExtracter():
    def __init__(self, filenames=None,  preprocessor=simpleSplit):
        self.filenames = filenames
        self.preprocessor = preprocessor
        # self.columns = ["id", "title", "abstract"]
        # self.df = pd.DataFrame(columns=self.columns)
        self.df = pd.DataFrame()
        # self.tempdf = pd.DataFrame(columns=self.columns)

    
    def JsonCleaner(self, filename, lemma = True):
        print(filename)
        dataarray = []
        idarray = []
        with open(filename, "r") as fd:
            line = fd.readline()
            while line != "":
                if line.find("bibo:abstract") != -1 and line.find("bibo:shortTitle") != -1 and line.find("identifier") != -1:
                    jsonobj = json.loads(line)
                    identifier = jsonobj["identifier"]
                    if identifier not in idarray:
                        idarray.append(identifier)
                        # print(id)
                        title = jsonobj["bibo:shortTitle"] 
                        preabstract = jsonobj["bibo:abstract"]
                        abstract = self.preprocessor.preprocess(preabstract, to_lemmatize=lemma)
                        if len(abstract) > 5:
                            data = {"id":identifier, "title":title, "abstract":abstract}
                            dataarray.append(data)
                    
                    # print(str(id) + "Type of id: " + str(type(id)))
                    # print(title + "Type of title: " + str(type(title)))
                    # print(abstract + "Type of abstract: " + str(type(abstract)))
                    # print(id, pretitle, title, abstract, sep="\n")

                line = fd.readline()
        print("datarr: ", len(dataarray))
        self.df = pd.DataFrame(dataarray)
        # temp = self.df.append(dataarray, ignore_index=True)
        # self.df = temp
        print("df.index: ", len(self.df.index))

    def FilesCleaner(self):
        for filename in self.filenames:
            self.JsonCleaner(filename)
            csvname = "./cleaned/" + filename.rsplit(".")[0] + ".csv"
            self.df.to_csv(csvname, index=False)
            # self.df = pd.DataFrame(columns=self.columns)            
        pass


if __name__ == "__main__":
    filenames = sorted(os.listdir())
    new = [f for f in filenames if f[-4:] == "json"]
    filenames = new

    # op = "repository_metadata_2_2013-03-18.csv"
    pre = AbstractPreprocessor()
    AbsExt = AbstractExtracter(filenames,pre)
    AbsExt.FilesCleaner()
    # df = pd.read_csv(op)
    # print(df)
    pass