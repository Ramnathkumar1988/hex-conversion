#!/usr/bin/env python
import os
import csv
import requests
import json
from datetime import datetime, timedelta
r=datetime.today()

bag_of_words_directory="C:\Users\Ram\Desktop\python"

# splits text to set of words
def split_text(input_string):
    splited_set=input_string.split()
    return splited_set

# Converts files to set
def file_to_set(file):
    f = open(file, 'r')
    word_set = split_text(f.read())
    f.close()
    return word_set

# percentage calculation
def percentage(part, whole):
    try:
        return ((100 * float(part))/float(whole))
    except ZeroDivisionError:
        return 0

#the main calculation function
def sentiment_analysis(input_text):
    positive_count = 0
    negative_count = 0

    positive_matches = set(A1) & set(split_text(input_text))
    positive_count = len(positive_matches)
    #positive_score = positive_count * 2

    negative_matches = set(A2) & set(split_text(input_text))
    negative_count = len(negative_matches)
    #negative_score = negative_count * 2

    if positive_count >= negative_count:
        adverb_matches = set(B) & set(split_text(input_text))
        positive_score = positive_score + len(adverb_matches)
    else:
        adverb_matches = set(B) & set(split_text(input_text))
        negative_score = negative_score + len(adverb_matches)
    print("-------- results after matching the adverbs :")
    positive_score_percentage = percentage(positive_score,positive_score+negative_score)
    negative_score_percentage = percentage(negative_score,positive_score+negative_score)

    print(" - pos:"+str(positive_score)+" - neg:"+str(negative_score))
    print(" - positive:"+str(positive_score_percentage)+" - neg:"+str(negative_score_percentage))

    return positive_score_percentage,negative_score_percentage

# initial basic sets for application
A1 = file_to_set(bag_of_words_directory+"/positive-words.txt")
A2 = file_to_set(bag_of_words_directory+"/negative-words.txt")
B = file_to_set(bag_of_words_directory+"/adverb.txt")

for i in range (0,30):
    r1 = r - timedelta(days=i)
    r1 = r1.strftime('%y-%m-%d')
    url = 'https://newsapi.org/v2/everything?q=amazon&sources=fortune&from='+r1+'&to='+r1+'&apiKey=b3bf7ec3600f4a4eb04c2171473017a6'
    response = requests.get(url)
    json_data = json.loads(response.text)
    for item in json_data["articles"]:
        print (r1, item["content"])
        if item["content"] != None:
            print(sentiment_analysis(item["content"]))
