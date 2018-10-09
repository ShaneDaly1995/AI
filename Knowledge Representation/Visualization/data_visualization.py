#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:00:03 2018

@author: shanedaly
"""

import numpy as np
import pandas as pd

def main():
    read_parse("adult.csv")
    
def read_parse(file_name):
    adult_df = pd.read_csv(file_name)
    
    # Q1 a
    adult_df = adult_df.replace('?', np.nan)    
    
    #Q1 b
    print("\nNaN's present:")
    print((adult_df.isin([np.nan]).sum()), "\n")
    
    #Q1 c 
    adult_df = adult_df.dropna()
    print("NaN's removed:")
    print((adult_df.isin([np.nan]).sum()), "\n")

    # Q2 a
    new_df1 = adult_df[['gender','educational-num']]
    new_df1 = new_df1.groupby(['gender']).mean()
    print(new_df1)
    
    #Q2 b
    print("\n")
    gender_df = adult_df[['gender', 'income']]
    gender_df = gender_df.groupby(['gender', 'income'])
    gender_count = adult_df['gender'].value_counts()
    
    
    
    
    
main()