## This parser transforms chart data from csv to  pipe format in txt
## e.g
# Data from dataset_barchart/data/1.csv
# will be converted to 
#  Age_Group|Under_25|x|bar_chart Revenue_share|7.3|y|bar_chart Age_Group|25-44|x|bar_chart Revenue_share|33.1|y|bar_chart Age_Group|45-64|x|bar_chart Revenue_share|43.5|y|bar_chart Age_Group|65_and_over|x|bar_chart Revenue_share|16.1|y|bar_chart

import csv
import os
import pandas as pd
import re

def openData(dataPath):
    df = pd.read_csv(dataPath)
    cols = df.columns
    size = df.shape[0]
    xAxis = cols[0]
    yAxis = cols[1]
    return df, cols, size, xAxis, yAxis

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

dataFiles = os.listdir('./dataset_barchart/data')
dataFiles = [int(i.split('.')[0]) for i in dataFiles]
dataFiles.sort()

dataArr = []

for i in range(len(dataFiles)):
    dataPath = './dataset_barchart/data/' + str(dataFiles[i]) + '.csv'

    df, cols, size, xAxis, yAxis = openData(dataPath)
    cleanXAxis = cleanAxisLabel(xAxis)
    cleanYAxis = cleanAxisLabel(yAxis)
    dataLine = ''
    for m in range(0, size):
        xValue = str(df.at[m, xAxis])
        yValue = str(df.at[m, yAxis])

        cleanXValue = cleanAxisValue(xValue)
        cleanYValue = cleanAxisValue(yValue)

        xRecord = cleanXAxis + '|' + cleanXValue + '|' + 'x' + '|' + chartType
        yRecord = cleanYAxis + '|' + cleanYValue + '|' + 'y' + '|' + chartType
        dataLine = dataLine + xRecord + ' ' + yRecord + ' '
    
    dataArr.append(dataLine)


with open('./dataset_barchart/data.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s\n" % line for line in dataArr)

print(len(dataFiles))