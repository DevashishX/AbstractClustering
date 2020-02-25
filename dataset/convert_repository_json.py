import json
import numpy as np
import pandas as pd
from pprint import pprint
from preprocessing import AbstractPreprocessor, preproc

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
        self.columns = ["id", "title", "abstract"]
        self.df = pd.DataFrame(columns=self.columns)
        self.tempdf = pd.DataFrame(columns=self.columns)

    
    def JsonCleaner(self, filename, lemma = True):
        dataarray = []
        idarray = []
        with open(filename, "r") as fd:
            line = fd.readline()
            while line != "":
                if line.find("bibo:abstract") != -1:
                    jsonobj = json.loads(line)
                    id = jsonobj["identifier"]
                    if id not in idarray:
                        idarray.append(id)
                        # print(id)
                        title = jsonobj["bibo:shortTitle"] 
                        preabstract = jsonobj["bibo:abstract"]
                        abstract = self.preprocessor.preprocess(preabstract, to_lemmatize=lemma)
                        data = {"id":id, "title":title, "abstract":abstract}
                        dataarray.append(data)
                    
                    # print(str(id) + "Type of id: " + str(type(id)))
                    # print(title + "Type of title: " + str(type(title)))
                    # print(abstract + "Type of abstract: " + str(type(abstract)))
                    # print(id, pretitle, title, abstract, sep="\n")

                line = fd.readline()        
        self.df = self.df.append(dataarray, ignore_index=True)

    def FilesCleaner(self):
        for filename in self.filenames:
            self.JsonCleaner(filename)
            csvname = filename.rsplit(".")[0] + ".csv"
            self.df.to_csv(csvname, index=False)
            # csvname = filename.rsplit(".")[0] + ".pkl"
            # self.df.to_pickle(csvname)
        pass


if __name__ == "__main__":
    filenames = ["repository_metadata_2_2013-03-18.json"]
    op = "repository_metadata_2_2013-03-18.csv"
    pre = AbstractPreprocessor()
    AbsExt = AbstractExtracter(filenames,pre)
    AbsExt.FilesCleaner()
    # df = pd.read_csv(op)
    # print(df)
    pass