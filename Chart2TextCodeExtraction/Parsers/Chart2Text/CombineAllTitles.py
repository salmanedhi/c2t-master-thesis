## This file combines all titles from directory into one txt file

import csv
import os
import pandas as pd
import re

def openCaption(captionPath):
    with open(captionPath, 'r', encoding='utf-8') as captionFile:
        caption = captionFile.read()
    return caption

def cleanAxisValue(value):
    #print(value)
    if value == '-' or value == 'nan':
        return '0'
    cleanValue = re.sub('\s', '_', value)
    cleanValue = cleanValue.replace('|', '').replace(',', '').replace('%', '').replace('*', '')
    return cleanValue


def cleanAxisLabel(label):
    cleanLabel = re.sub('\s', '_', label)
    cleanLabel = cleanLabel.replace('%', '').replace('*', '')
    return cleanLabel


chartType = 'bar_chart'

titleFiles = os.listdir('../../dataset_barchart/titles')
titleFiles = [int(i.split('.')[0]) for i in titleFiles]
titleFiles.sort()

titleArr = []

for i in range(len(titleFiles)):
    dataPath = '../../dataset_barchart/titles/' + str(titleFiles[i]) + '.txt'

    title = openCaption(dataPath)
    titleArr.append(title)

with open('../../dataset_barchart/titles.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in titleArr)

print(len(titleArr))