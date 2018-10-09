# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Padraigh Jarvis
"""

#Delcaring positive and negative dict as global for future use
positive_dict = {}
negative_dict = {}

#Import maths for using log
import math 

#Count how many times a word occured in one of the files and add it to a dictionary passed in
def populateFrequency(dictionary,wordList):
    for word in wordList:
        dictionary[word] = dictionary[word] + 1
    return dictionary    

#Calculate the probablilty of a word being positive or negative and populating an entire dictionary with it
def populateProbablility(dictionary, vocabCount):
    total_words = sum(dictionary.values())
    for word in dictionary:
        dictionary[word] = math.log(( dictionary[word]+1) / (total_words + vocabCount))
    return dictionary

#Read contents of a file passed in and returns it after it has been converted to lower case 
def readFile(fileName):
    file = open(fileName,'r', encoding = "ISO-8859-1")    
    contents = file.read()
    file.close()
    contents = contents.lower()
    return contents

#Retrieves training data from file and splits it by whitespace
def getTrainText(fileName):
    contents = readFile(fileName)
    contents = contents.split()
    return contents

#Retrieves tet data from file and splits it by new line
def getTestText(fileName):
    contents = readFile(fileName)
    contents = contents.split("\n")
    return contents

def train():
    #Declare dictionarys and vocab
    global positive_dict, negative_dict
    vocab = set()
    
    #Read in training data into a list of words split by whitespace
    positiveList = getTrainText("dataset/train/trainPos.txt")
    negativeList = getTrainText("dataset/train/trainNeg.txt")
    
    #Populate the unique vocabulary with the contents of the positive and negative words
    vocab.update(positiveList)
    vocab.update(negativeList)
    
    #Create a entry in the pos and neg dictionary for each word in our vocab
    positive_dict = dict.fromkeys(vocab,0)
    negative_dict = dict.fromkeys(vocab,0)
    
    #Replace the contents of the pos and neg dict with the number of times each word occured
    positive_dict = populateFrequency(positive_dict, positiveList)
    negative_dict = populateFrequency(negative_dict, negativeList)
    
    #Find the total number of unique words for the probablility calculation
    vocab_count = len(vocab)
    
    #Calculate the probablity of each word in both dictionaries
    positive_dict = populateProbablility(positive_dict, vocab_count)
    negative_dict = populateProbablility(negative_dict, vocab_count)

    


def test():
    #Reads in test data, each item in the array is a tweet
    positive_test_contents = getTestText("dataset/test/testPos.txt")
    negative_test_contents = getTestText("dataset/test/testNeg.txt")
    
    print(len(positive_test_contents), len(negative_test_contents))
    
    #Finds the actual number of tweets that are negative or positive ie all tweets in the testPos file etc
    true_positive_count = len(positive_test_contents)
    true_negative_count = len(negative_test_contents)
    
    #Calculate the sentiment for positive unseen tweets
    test_positive_count = 0
    for tweet in positive_test_contents:
        #Declare a variable for positive and negative sentiment
        positive_tweet_sentiment=0.0
        negative_tweet_sentiment=0.0
        #Split the tweet so we can look at the posibility for each word being positive or negative
        tweet_contents = tweet.split()
        
        for word in tweet_contents:
            #if the word is present in the positive dictionary then add the posibility of that word being positive to the overall tweet positive sentiment
            if word in positive_dict:
                positive_tweet_sentiment= positive_tweet_sentiment + positive_dict[word]
            #if the word is present in the negative dictionary then add the posibility of that word being positive to the overall tweet negative sentiment
            if word in negative_dict:
                negative_tweet_sentiment = negative_tweet_sentiment + negative_dict[word]
        #If the number for the positive tweet sentiment is higher then the negative tweet sentiment then it has been classifed as positive sentiment
        if positive_tweet_sentiment > negative_tweet_sentiment:
            test_positive_count = test_positive_count + 1
    #Print out the level of positive accuracy
    print("Level of positive accuracy:{}%".format((test_positive_count/true_positive_count)*100))
    
    #Calculate the sentiment for negative unseen tweets 
    test_negative_count = 0
    for tweet in negative_test_contents:
        #Declare a variable for positive and negative sentiment
        positive_tweet_sentiment=0.0
        negative_tweet_sentiment=0.0
        
        #Split the tweet so we can look at the posibility for each word being positive or negative
        tweet_contents = tweet.split()
        
        for word in tweet_contents:
            #if the word is present in the positive dictionary then add the posibility of that word being positive to the overall tweet positive sentiment
            if word in positive_dict:
                positive_tweet_sentiment= positive_tweet_sentiment + positive_dict[word]
            #if the word is present in the negative dictionary then add the posibility of that word being negative to the overall tweet negative sentiment
            if word in negative_dict:
                negative_tweet_sentiment = negative_tweet_sentiment + negative_dict[word]
        #If the number for the negative tweet sentiment is higher then the positive tweet sentiment then it has been classifed as negative sentiment
        if positive_tweet_sentiment < negative_tweet_sentiment:
            test_negative_count = test_negative_count + 1
    #Print out the level of negative accuracy        
    print("Level of negative accuracy:{}%".format((test_negative_count/true_negative_count)*100))
    
    
    
    
def main():
    #Train our model
    train()
    #Test our model
    test()
    
main()