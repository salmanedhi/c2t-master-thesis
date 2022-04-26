# this file copies only bar charts from the complete original dataset of Chart2text
# this file was used once to copy all the barchart files from dataset_original to dataset_barchart
import os
import shutil
import pandas as pd


def getChartType(x):
    if x.lower() == 'year':
        return 'line_chart'
    else:
        return 'bar_chart'

def openData(dataPath):
    df = pd.read_csv(dataPath)
    cols = df.columns
    size = df.shape[0]
    xAxis = cols[0]
    yAxis = cols[1]
    chartType = getChartType(xAxis)
    return df, cols, size, xAxis, yAxis, chartType

## calling main function
dataFiles = os.listdir('./dataset_original/data')
dataFiles.sort()
# dataFiles = dataFiles[0:2]

captionFiles = os.listdir('./dataset_original/captions')
captionFiles.sort()
# captionFiles = captionFiles[0:2]

titleFiles = os.listdir('./dataset_original/titles')
titleFiles.sort()
# titleFiles = titleFiles[0:2]

assert len(captionFiles) == len(dataFiles) == len(titleFiles)
print(len(captionFiles), len(dataFiles), len(titleFiles))

count = 0

for m in range(len(dataFiles)):
    dataPath = './dataset_original/data/' + dataFiles[m]
    captionPath = './dataset_original/captions/' + captionFiles[m]
    titlePath = './dataset_original/titles/' + titleFiles[m]

    targetDataPath = './dataset_barchart/data/' + dataFiles[m]
    targetCaptionPath = './dataset_barchart/captions/' + captionFiles[m]
    targetTitlePath = './dataset_barchart/titles/' + titleFiles[m]

    df, cols, size, xAxis, yAxis, chartType = openData(dataPath)

    if(chartType == 'bar_chart'):
        count = count+1
        shutil.copyfile(dataPath, targetDataPath)
        shutil.copyfile(captionPath, targetCaptionPath)
        shutil.copyfile(titlePath, targetTitlePath)

print(count)


