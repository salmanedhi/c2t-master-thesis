#### This is to select specific iza data in the order iza and I decided so that we have the same training and test data
import os
import shutil
import pandas as pd
from sklearn import utils
import json

def openCaption(captionPath):
    with open(captionPath, 'r', encoding='utf-8') as captionFile:
        caption = captionFile.readlines()
    return caption

mainSourcePath = '../Chart2Text-Basic-IzaEdition/data/'


# VALID DATA
finalSummaryLabels = []
summaries = openCaption(mainSourcePath + 'valid/validSummary.txt')
summariesLabel = openCaption(mainSourcePath + 'valid/validSummaryLabel.txt')

assert(len(summaries) == len(summariesLabel))
for m in range(len(summaries)):
    summary = summaries[m]
    summaryArr = summary.split()
    summaryLabel = summariesLabel[m]
    summaryLabelArr = summaryLabel.split()
    # print(summaryLabelArr)
    finalSummaryLabel = summaryLabel.rstrip("\n")
    if(len(summaryArr) > len(summaryLabelArr)):
        for i in range(0, len(summaryArr) - len(summaryLabelArr)):
            finalSummaryLabel = finalSummaryLabel + ' 0'
    elif(len(summaryArr) < len(summaryLabelArr)):
        finalSummaryLabel = ""
        for i in range(0, len(summaryArr)):
            finalSummaryLabel = finalSummaryLabel + " " + summaryLabelArr[i].rstrip("\n")
    elif(len(summaryArr) == len(summaryLabelArr)):
        finalSummaryLabel = ""
        for i in range(0, len(summaryArr)):
            finalSummaryLabel = finalSummaryLabel + " " + summaryLabelArr[i].rstrip("\n")

    finalSummaryLabels.append(finalSummaryLabel.strip())

with open(mainSourcePath + 'valid/validSummaryLabel.txt', "w") as data_file:
    for data in finalSummaryLabels:
        data_file.write(data + "\n")

# TEST DATA
finalSummaryLabels = []
summaries = openCaption(mainSourcePath + 'test/testSummary.txt')
summariesLabel = openCaption(mainSourcePath + 'test/testSummaryLabel.txt')

assert(len(summaries) == len(summariesLabel))
for m in range(len(summaries)):
    summary = summaries[m]
    summaryArr = summary.split()
    summaryLabel = summariesLabel[m]
    summaryLabelArr = summaryLabel.split()
    # print(summaryLabelArr)
    finalSummaryLabel = summaryLabel.rstrip("\n")
    if(len(summaryArr) > len(summaryLabelArr)):
        for i in range(0, len(summaryArr) - len(summaryLabelArr)):
            finalSummaryLabel = finalSummaryLabel + ' 0'
    elif(len(summaryArr) < len(summaryLabelArr)):
        finalSummaryLabel = ""
        for i in range(0, len(summaryArr)):
            finalSummaryLabel = finalSummaryLabel + " " + summaryLabelArr[i].rstrip("\n")
    elif(len(summaryArr) == len(summaryLabelArr)):
        finalSummaryLabel = ""
        for i in range(0, len(summaryArr)):
            finalSummaryLabel = finalSummaryLabel + " " + summaryLabelArr[i].rstrip("\n")

    finalSummaryLabels.append(finalSummaryLabel.strip())

with open(mainSourcePath + 'test/testSummaryLabel.txt', "w") as data_file:
    for data in finalSummaryLabels:
        data_file.write(data + "\n")

# TRAIN DATA
finalSummaryLabels = []
summaries = openCaption(mainSourcePath + 'train/trainSummary.txt')
summariesLabel = openCaption(mainSourcePath + 'train/trainSummaryLabel.txt')

assert(len(summaries) == len(summariesLabel))
for m in range(len(summaries)):
    summary = summaries[m]
    summaryArr = summary.split()
    summaryLabel = summariesLabel[m]
    summaryLabelArr = summaryLabel.split()
    # print(summaryLabelArr)
    finalSummaryLabel = summaryLabel.rstrip("\n")
    if(len(summaryArr) > len(summaryLabelArr)):
        for i in range(0, len(summaryArr) - len(summaryLabelArr)):
            finalSummaryLabel = finalSummaryLabel + ' 0'
    elif(len(summaryArr) < len(summaryLabelArr)):
        finalSummaryLabel = ""
        for i in range(0, len(summaryArr)):
            finalSummaryLabel = finalSummaryLabel + " " + summaryLabelArr[i].rstrip("\n")
    elif(len(summaryArr) == len(summaryLabelArr)):
        finalSummaryLabel = ""
        for i in range(0, len(summaryArr)):
            finalSummaryLabel = finalSummaryLabel + " " + summaryLabelArr[i].rstrip("\n")

    finalSummaryLabels.append(finalSummaryLabel.strip())

with open(mainSourcePath + 'train/trainSummaryLabel.txt', "w") as data_file:
    for data in finalSummaryLabels:
        data_file.write(data + "\n")

