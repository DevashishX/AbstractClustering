"""
This is the preproceing function
"""
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

def preproc(text, to_lemmatize = False):
    # text = str(text)
    # words = word_tokenize(text.lower())
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    stopword_filtered_list = [w for w in words if w not in stop_words]
    final_list = stopword_filtered_list
    if to_lemmatize :
        lemmatizer = WordNetLemmatizer()
        final_list = [lemmatizer.lemmatize(w) for w in stopword_filtered_list]
    return final_list

class AbstractPreprocessor():
    def __init__(self, pattern = r'\w+'):
        self.tokenizer = RegexpTokenizer(pattern)
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

        pass

    def preprocess(self, text, to_lemmatize=False):
        words = self.tokenizer.tokenize(text.lower())
        stopword_filtered_list = [w for w in words if w not in self.stop_words]
        number_filtered_list = [w for w in stopword_filtered_list if not w.isdigit()]
        final_list = number_filtered_list
        if to_lemmatize:
            final_list = [self.lemmatizer.lemmatize(w) for w in number_filtered_list]
        return final_list