import pandas as pd
import csv
from nltk.corpus import wordnet
import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')


def extract_salary(string):
    r = re.compile(r'[\$]{1}[\d,]+\.?\d{0,2}')
    salary = r.findall(string)
    return [re.sub(r'^[0-9]\d{0,9}(\.\d{1,3})?%?$', '', number) for number in salary]

def extract_date(string):
    r = re.compile(r'[A-Z][a-z]{2}\s\d{2},\s\d{4}')
    dat = r.findall(string)
    return dat

def extract_position():
    with open('N:/Research/RW/Employee Contracts/pgm/2178_2004-11-12_EXHIBIT 10.1 EMPLOYMENT AGREEMENT.txt', 'r', encoding='latin-1') as f:
        lines = f.readlines()  # read all lines into a list
        for index, line in enumerate(lines):  # enumerate the list and loop through it
            if "employs" in line:  # check if the current line has your substring
                s = line.split('and')  # print the current line (stripped off whitespace)
                return(s[1])

def extract_notice_period():
    with open('N:/Research/RW/Employee Contracts/pgm/2178_2004-11-12_EXHIBIT 10.1 EMPLOYMENT AGREEMENT.txt', 'r', encoding='latin-1') as f:
        lines = f.readlines()  # read all lines into a list
        for index, line in enumerate(lines):  # enumerate the list and loop through it
            if "notice" in line:  # check if the current line has your substring
                s = re.split('upon |prior',line)  # print the current line (stripped off whitespace)
                return(s)

person_list = []
person_names=person_list
def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)

    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

if __name__ == '__main__':
    with open('N:/Research/RW/Employee Contracts/pgm/2178_2004-11-12_EXHIBIT 10.1 EMPLOYMENT AGREEMENT.txt', 'r', encoding='latin-1') as f:
        sample = f.read()

    #Employee - Employer Information
    names = get_human_names(sample)
    for person in person_list:
        person_split = person.split(" ")
        for name in person_split:
            if wordnet.synsets(name):
                if (name in person):
                    person_names.remove(person)
                    break

    # Salary Information
    sal = extract_salary(sample)

    # Date Information
    dat = extract_date(sample)

    #Position Information
    posn = extract_position()

    #Notice Period Information
    ntce = extract_notice_period()

    # Define a dictionary containing employee data
    data = {'Name of the Employee': [person_names[0]],
            'Name of the Employer': [person_names[2]],
            'Date of Agreement': [dat[0]],
            'Job Title': [posn],
            'Base Salary': [sal[0]],
            'Employment Start Date': [dat[1]],
            'Employment End Date': [dat[2]],
            'Bonus': [sal[3]],
            'Notice Period': [ntce[1]]}

    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)

    #Writing a dictionary data (key, value) to a CSV file - datas.csv
    with open('N:/Research/RW/Employee Contracts/pgm/model2/datas.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in data.items():
            writer.writerow([key, value])