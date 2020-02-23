"""
This is the preproceing function
"""
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

def preproc(text, to_lemmatize = False):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    stopword_filtered_list = [w for w in words if w not in stop_words]
    final_list = stopword_filtered_list
    if to_lemmatize :
        lemmatizer = WordNetLemmatizer()
        final_list = [lemmatizer.lemmatize(w) for w in stopword_filtered_list]
    return final_list
