
# -*- coding: utf-8 -*-
import sys
import operator
import requests
import json
from watson_developer_cloud import PersonalityInsightsV2 as PerIns
import bs4
from scipy.spatial.distance import cosine
import nltk


# Function to request and receive the contents of a webpage
# throws and exception if finds a problem, it is used to 
# scrape the web for information.
def fetch(address):
    res = requests.get(address)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    if res.status_code == requests.codes.ok:
        print "OK"
    return res


# Html to text parsing function, with specific parameters
# with a selection of parameters depending on the web page
# being scrapped. It also can save the file to file.txt
# used for http://www.dailyscript.com/ and
# http://www.imsdb.com/ 
def htmlToTxt(res,name,save=False,opt=False):
    soup   = bs4.BeautifulSoup(res.text,'lxml')
    clean_script = ''
    
    if opt:
        tdtext = soup.find_all('td',class_='scrtext')
    else:
        tdtext = soup.find_all('body')

    for i in tdtext:
        clean_script += i.pre.get_text().encode('utf8')
    
    if save:
        f = open('scrapped/'+name+'.txt','w')
        f.write(temp)
        f.close()
        
    return clean_script


# Function to read a text file from disk using the name of
# the movie    
def readTxt(name):
    with open(name+'.txt','r') as f:
        lines = f.readlines()
    return lines


# Helper function to change dictionary to list
def dToL(dict1):
    return [dict1.values(),dict1.keys()]


# Scripts come with all the action and environment indications
# in CAPS, this can have an impact on the model and should 
# ponder to include them or not, if not, this is the function
# for removing them
def removeCAPS(script):
    temp = ''
    
    for i in range(len(script)-1):
        if script[i] == ' ' or script[i].islower() or (script[i].isupper() and script[i+1].islower()):
            temp += script[i]
    
    return ' '.join(temp.split())


# Compares to dictionaries, this is primarily used when receiving
# the results from the Watson API personality insights, don't think
# I'll be using it much
def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
                compared_data[keys]=abs(dict1[keys] - dict2[keys])
    return compared_data


# Watson API returns information that for now will not be used
# this function flattens the dictionary to a single level and 
# only keeps the data needed
def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data


# Function to make the request to the Watson API, it takes 
# a user name and password (obtained by registering for free)
# on its website
def insight(text,user,password):
    connect = PerIns(username=user,password=password)
    return connect.profile(text)


# Similarity returns the cosine similarity between two lists of
# numbers, it used to find similarities, for example, between
# movies using their genres, or in this cases, the results
# from Watson's API                                              
def similarity(list1,list2):                             
    return 1.-cosine(list1,list2) 


# Another parsing function, this one for http://www.springfieldspringfield.co.uk/
def springScrap(raw):
    result = ' '
    soup = bs4.BeautifulSoup(raw.text,'lxml')
    for e in soup.findAll('br'):
        e.extract()
    for text in soup.find_all('div',class_='scrolling-script-container'):
        result += text.get_text().encode('utf8')
    return result


# OMDB allows to extract basic imdb infomation that will be user as meta-data
# for the regression models, transform from json to dictionary
def omdb(tag=None,name=None):
    if tag:
        url = 'http://www.omdbapi.com/?i='+tag+'&plot=short&r=json'
        raw = fetch(url)
    else:
        url = "http://www.omdbapi.com/?t="+name+"&y=&plot=short&r=json"
        raw = fetch(url)
    result = ''
    for i in raw:
        result += i 
    return json.loads(result)


# Text Analytics, to be greatly improved, by now it extracts some information
# like no. of words, diversity of words and noun/verb ratio
def words(script):
    tokens    = nltk.word_tokenize(script)
    nwords    = len(tokens)
    diversity = len(set(tokens))/float(nwords)
    tagger    = nltk.pos_tag(tokens,tagset='universal')
    counter = [0.,0.]
    for i in tagger:
        if i[1] == 'VERB':
            counter[0] += 1.
        if i[1] == 'NOUN':
            counter[1] += 1.
    return [nwords,diversity,counter[1]/counter[0]]


# Homebrew splitter train/test
def train_test(x,size=0.7,boot=False):
    r = range(len(x))
    train = sorted(np.random.choice(r,size= int(len(x)*size),replace=boot))
    test = []
    for i in r:
        if i not in train:
            test.append(i)
    return train, test