#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:28:02 2018

@author: shanedaly
"""
import math

tweets_pos = []
tweets_neg = []
pos_dict = {}
neg_dict = {}

test_pos = []
test_neg = []

vocab = set()

def main():
    train()
    test()

def train():
    tweets_pos, tweets_neg, vocab = open_read()
    create_dictionary(tweets_pos, tweets_neg)
    calculate_probability(pos_dict, vocab)
    calculate_probability(neg_dict, vocab)
    
def open_read():
    f = open("dataset/train/trainPos.txt", "r", encoding="ISO-8859-1")
    tweets_pos = f.read()
    f.close()
    tweets_pos = tweets_pos.lower()
    tweets_pos = tweets_pos.split()
    
    g = open("dataset/train/trainNeg.txt", "r", encoding="ISO-8859-1")
    tweets_neg = g.read()
    g.close()
    tweets_neg = tweets_neg.lower()
    tweets_neg = tweets_neg.split()
    
    print(tweets_neg)
    vocab.update(tweets_pos)
    vocab.update(tweets_neg)

    return tweets_pos, tweets_neg, vocab
    
def create_dictionary(tweets_pos, tweets_neg):
    global pos_dict, neg_dict
    
    pos_dict = dict.fromkeys(tweets_pos, 0)
    occurrences(tweets_pos, pos_dict)
    
    neg_dict = dict.fromkeys(tweets_neg, 0)
    occurrences(tweets_neg, neg_dict)
    
def occurrences(a_list, a_dict):
    
    for word in a_list:
        a_dict[word] += 1
    return a_dict
    
    
def calculate_probability(data, vocab):
    
    val = sum(data.values())
    the_count = len(vocab)
    for word in data:
        data[word] = math.log((data[word] +1) / (val + the_count))
    return data
        
# -------------------------------------------------------------------------

def test():
    test_pos, test_neg = classify_unseen()
    test_dictionaries(test_pos, test_neg)
    
    
    
def classify_unseen():
    
    h = open("dataset/test/testPos.txt", "r", encoding="ISO-8859-1")
    test_pos = h.read()
    h.close()
    test_pos = test_pos.lower()
    test_pos = test_pos.split("\n")
    
    i = open("dataset/test/testNeg.txt", "r", encoding="ISO-8859-1")
    test_neg = i.read()
    i.close()
    test_neg = test_neg.lower()
    test_neg = test_neg.split("\n")
    
    
    return test_pos, test_neg
    
    
def test_dictionaries(test_pos, test_neg):
   
    positive_tweet_count = 0
    negative_tweet_count = 0 
    
    len_test_pos = len(test_pos)
    len_test_neg = len(test_neg)
    
    # split the tweets 
    for tweets in test_pos:
       
        positive_tweets = 0.0
        negative_tweets = 0.0
        
        tweet_words = tweets.split(" ")
        
        for word in tweet_words:
            if word in pos_dict:
                positive_tweets = positive_tweets + pos_dict[word]
            
            if word in neg_dict:
                negative_tweets = negative_tweets + neg_dict[word]
                
            
        if positive_tweets > negative_tweets:
                positive_tweet_count = positive_tweet_count + 1
    print("Positive accuracy: {:.2f}%".format((positive_tweet_count/len_test_pos)*100))          
                
    for tweets in test_neg:
        positive_tweets = 0
        negative_tweets = 0
        
        tweet_words = tweets.split(" ")
        
        for word in tweet_words:
            if word in pos_dict:
                positive_tweets = positive_tweets + pos_dict[word]
                
            if word in neg_dict:
                negative_tweets = negative_tweets + neg_dict[word]
                
        if negative_tweets > positive_tweets:
            negative_tweet_count = negative_tweet_count + 1
    
    print("Negative accuracy: {:.2f}%".format((negative_tweet_count/len_test_neg)*100))          

main()
    