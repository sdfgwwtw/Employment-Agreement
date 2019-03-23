import pandas as pd
import csv
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

def stop_filter(words):
    stops = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than', 'r', 'e', 'd', 'm', 'n', 'o', '4', '1', '2', '3', '5', 'abbreviation', 'review', '6', '7', '8', '2']
    word_token = words.lower()
    word_tokens = word_tokenize(word_token)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stops:
            filtered_sentence.append(w)
    return filtered_sentence

#tokenization - stemmming
tokens_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    st_tokens = ''
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tsplit(s, sep):
    stack = [s]
    for char in sep:
        pieces = []
        for substr in stack:
            pieces.extend(substr.split(char))
        stack = pieces
    return stack


lst = list()

#removal of stop words
with open('N:/Research/RW/Employee Contracts/pgm/dataset/files/dataset.csv', 'r')as tr:
    train = csv.reader(tr)
    for r in train:
        s = str(r)
        for rps in tsplit(s, ("..", "EXHIBIT","-")):
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~[0-9]'''
            # remove punctuation from the string
            no_punct = ""
            for char in rps:
                if char not in punctuations:
                    no_punct = no_punct + char
            models = stop_filter(no_punct)
            ste = stem_tokens(models, stemmer)
            sent_str = " "
            for i in ste:
                sent_str += str(i) + " "
            sent_str = sent_str[:-1]
            lst.append(sent_str)
#print(lst)
df = pd.DataFrame(lst)
df.to_csv("N:/Research/RW/Employee Contracts/pgm/dataset/files/clean_dataset.csv", encoding='utf-8', index=False, sep=' ', header=False)