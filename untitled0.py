#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:24:04 2017

@author: virajdeshwal
"""
import pandas as pd
import numpy as np
import csv
from collections import Counter


sorted_list=[]
    
data1 = pd.read_csv('sample.csv')

X = np.array(data[["tasker_id"]])
for lines, index in enumerate(X):
    print(lines, index)
        
        
   
#unique = np.unique(X)
#for lines, index in enumerate(unique):
    #print(lines, index)
    


    