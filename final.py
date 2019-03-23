import pandas as pd
from textblob.classifiers import NaiveBayesClassifier
import re
import random

def create_word_features(words):
    my_dict = dict( [ (word, True) for word in words] )
    return my_dict

amend = list()
emp_aggr = list()

shakes = open("N:/Research/RW/Employee Contracts/pgm/dataset/files/clean_dataset.csv", "r")
for line in shakes:
    if re.match("(.*)amend to employ agreement(.*)", line):
        amend.append((line, "amendment to employment agreement"))
    else:
        if re.match("(.*)employ agreement(.*)", line):
            emp_aggr.append((line, "employment agreement"))

# print(len(amend))
# print(amend)
# print(len(emp_aggr))
# print(emp_aggr)

combined_list = amend + emp_aggr
#print(len(combined_list))
random.shuffle(combined_list)
training_part = int(len(combined_list) * .7)
training_set = combined_list[:training_part]
test_set = combined_list[training_part:]

ts_df = pd.DataFrame(test_set)
ts_df["ts_label"] = ts_df[1].values
#print(ts_df["ts_label"])

#training is being done!!!
cl = NaiveBayesClassifier(training_set)
#print(cl)

#Creating list of probability distributions to extract probabilities from
probDist = []
for i in range(0, len(test_set)):
    probdist = cl.prob_classify(test_set[i][0])
    probDist.append(probdist)

#Creating list of the max probabilities for prediction
prob = []
for i in range(0, len(probDist)):
    prob.append(probDist[i].prob(probDist[i].max()))

#Creating list of predicted labels for test data
pred_labels = []
for i in range(0, len(test_set)):
    pred_labels.append(cl.classify(test_set[i][0]))

#print(pred_labels)
#test predicted features
tst_pred_fat = list()
for i in range(0, len(test_set)):
    tst_pred_fat.append((test_set[i], pred_labels[i]))


def model_evaluation(test_label, original_label):
    if len(test_label) != len(original_label):
        print('Error!! label length not equal')
        return ''
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(len(test_label)):
        if test_label[i] == 'amendment to employment agreement':
            if test_label[i] == original_label[i]:
                tn = tn + 1
            else:
                fn = fn + 1
        else:
            if test_label[i] == original_label[i]:
                tp = tp + 1
            else:
                fp = fp + 1
    p = tp + fn
    n = tn + fp
    recall = tp / p
    precision = tp / (tp + fp)
    return {
        'Total Test data:': len(test_label),
        'Correcly predicted': (tp + tn),
        'Wrong Predicted': len(test_label) - (tp + tn),
        'Accuracy': ((tp + tn) / (p + n)) * 100,
        'Error rate': ((fp + fn) / (p + n)) * 100,
        'Recall': recall,
        'precision': precision,
        'f1 score': (2 * precision * recall) / (precision + recall),
        'tpr': (tp / p),
        'fpr': (fp / n)
    }

print(model_evaluation(ts_df['ts_label'], pred_labels))