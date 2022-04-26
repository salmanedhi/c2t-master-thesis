# this file can be used to shuffle the dataset in 3 folders, captions, data, and titiles. 
import os
import shutil
import pandas as pd
from sklearn import utils

def openCaption(captionPath):
    with open(captionPath, 'r', encoding='utf-8') as captionFile:
        caption = captionFile.readlines()
    return caption

#### This is to shuffle only the Iza Data
# dataFiles = os.listdir('./Parsers/IzaDataToChartText/dataset/data')
# dataFiles.sort()
# # dataFiles = dataFiles[0:2]

# captionFiles = os.listdir('./Parsers/IzaDataToChartText/dataset/captions')
# captionFiles.sort()
# # captionFiles = captionFiles[0:2]

# titleFiles = os.listdir('./Parsers/IzaDataToChartText/dataset/titles')
# titleFiles.sort()
# # titleFiles = titleFiles[0:2]

# assert len(captionFiles) == len(dataFiles) == len(titleFiles)
# print(len(captionFiles), len(dataFiles), len(titleFiles))
# # print(titleFiles)

# dataFiles, captionFiles, titleFiles = utils.shuffle(dataFiles, captionFiles, titleFiles, random_state=0)

# idx = 1
# for m in range(len(dataFiles)):
#     dataPath = './Parsers/IzaDataToChartText/dataset/data/' + dataFiles[m]
#     captionPath = './Parsers/IzaDataToChartText/dataset/captions/' + captionFiles[m]
#     titlePath = './Parsers/IzaDataToChartText/dataset/titles/' + titleFiles[m]

#     targetDataPath = './Parsers/IzaDataToChartText/dataset/shuffled_data/' + str(idx) + '.csv'
#     targetCaptionPath = './Parsers/IzaDataToChartText/dataset/shuffled_captions/' + str(idx) + '.txt'
#     targetTitlePath = './Parsers/IzaDataToChartText/dataset/shuffled_titles/' + str(idx) + '.txt'

#     shutil.copyfile(dataPath, targetDataPath)
#     shutil.copyfile(captionPath, targetCaptionPath)
#     shutil.copyfile(titlePath, targetTitlePath)

#     idx = idx+1
#### Iza shuffle ends

#### this is to shuffle iza + bar data together
# izaDataFiles = os.listdir('./Parsers/IzaDataToChartText/dataset/data')
# izaDataFiles.sort()

# izaCaptionFiles = os.listdir('./Parsers/IzaDataToChartText/dataset/captions')
# izaCaptionFiles.sort()

# izaTitleFiles = os.listdir('./Parsers/IzaDataToChartText/dataset/titles')
# izaTitleFiles.sort()

# barDataFiles = os.listdir('./dataset_barchart/data')
# barDataFiles.sort()

# barCaptionFiles = os.listdir('./dataset_barchart/captions')
# barCaptionFiles.sort()

# barTitleFiles = os.listdir('./dataset_barchart/titles')
# barTitleFiles.sort()

# assert len(izaCaptionFiles) == len(izaDataFiles) == len(izaTitleFiles)
# print(len(izaCaptionFiles), len(izaDataFiles), len(izaTitleFiles))

# assert len(barDataFiles) == len(barCaptionFiles) == len(barTitleFiles)
# print(len(barDataFiles), len(barCaptionFiles), len(barTitleFiles))

# izaDataFiles, izaCaptionFiles, izaTitleFiles = utils.shuffle(izaDataFiles, izaCaptionFiles, izaTitleFiles, random_state=0)
# barDataFiles, barCaptionFiles, barTitleFiles = utils.shuffle(barDataFiles, barCaptionFiles, barTitleFiles, random_state=0)


# idx = 1
# for m in range(len(izaDataFiles)):
#     izaDataPath = './Parsers/IzaDataToChartText/dataset/data/' + izaDataFiles[m]
#     izaCaptionPath = './Parsers/IzaDataToChartText/dataset/captions/' + izaCaptionFiles[m]
#     izaTitlePath = './Parsers/IzaDataToChartText/dataset/titles/' + izaTitleFiles[m]

#     targetDataPath = './combined_dataset_bar_iza_shuffled/data/' + str(idx) + '.csv'
#     targetCaptionPath = './combined_dataset_bar_iza_shuffled/captions/' + str(idx) + '.txt'
#     targetTitlePath = './combined_dataset_bar_iza_shuffled/titles/' + str(idx) + '.txt'

#     shutil.copyfile(izaDataPath, targetDataPath)
#     shutil.copyfile(izaCaptionPath, targetCaptionPath)
#     shutil.copyfile(izaTitlePath, targetTitlePath)

#     idx = idx+1

# for m in range(len(barDataFiles)):
#     barDataPath = './dataset_barchart/data/' + barDataFiles[m]
#     barCaptionPath = './dataset_barchart/captions/' + barCaptionFiles[m]
#     barTitlePath = './dataset_barchart/titles/' + barTitleFiles[m]

#     targetDataPath = './combined_dataset_bar_iza_shuffled/data/' + str(idx) + '.csv'
#     targetCaptionPath = './combined_dataset_bar_iza_shuffled/captions/' + str(idx) + '.txt'
#     targetTitlePath = './combined_dataset_bar_iza_shuffled/titles/' + str(idx) + '.txt'

#     shutil.copyfile(barDataPath, targetDataPath)
#     shutil.copyfile(barCaptionPath, targetCaptionPath)
#     shutil.copyfile(barTitlePath, targetTitlePath)

#     idx = idx+1
#### this is to shuffle iza + bar data together

#### This is to shuffle once more the already shuffled iza and bar data
# dataFiles = os.listdir('./combined_dataset_bar_iza_shuffled/data')
# dataFiles.sort()
# # dataFiles = dataFiles[0:2]

# captionFiles = os.listdir('./combined_dataset_bar_iza_shuffled/captions')
# captionFiles.sort()
# # captionFiles = captionFiles[0:2]

# titleFiles = os.listdir('./combined_dataset_bar_iza_shuffled/titles')
# titleFiles.sort()
# # titleFiles = titleFiles[0:2]

# assert len(captionFiles) == len(dataFiles) == len(titleFiles)
# print(len(captionFiles), len(dataFiles), len(titleFiles))
# # print(titleFiles)

# dataFiles, captionFiles, titleFiles = utils.shuffle(dataFiles, captionFiles, titleFiles, random_state=0)

# idx = 1
# for m in range(len(dataFiles)):
#     dataPath = './combined_dataset_bar_iza_shuffled/data/' + dataFiles[m]
#     captionPath = './combined_dataset_bar_iza_shuffled/captions/' + captionFiles[m]
#     titlePath = './combined_dataset_bar_iza_shuffled/titles/' + titleFiles[m]

#     targetDataPath = './combined_dataset_bar_iza_shuffled/final_data/' + str(idx) + '.csv'
#     targetCaptionPath = './combined_dataset_bar_iza_shuffled/final_captions/' + str(idx) + '.txt'
#     targetTitlePath = './combined_dataset_bar_iza_shuffled/final_titles/' + str(idx) + '.txt'

#     shutil.copyfile(dataPath, targetDataPath)
#     shutil.copyfile(captionPath, targetCaptionPath)
#     shutil.copyfile(titlePath, targetTitlePath)

#     idx = idx+1
#### Iza shuffle ends


#### This is to select specific iza data in the order iza and I decided so that we have the same training and test data
trainIds = ["14_02-04", "07_02-11", "03_01-19", "01_02a-17", "09_01a-16", "01_01-11", "06_01-19", "11_02c-03", "01_02b-20", "10_01-16", "17_01a-13", "10_02-17", "08_01-07", "15_01b-05", "07_01-19", "09_02c-11", "06_01-13", "05_01c-11", "11_02c-22", "01_02a-15", "15_01a-21", "01_02c-10", "05_02-21", "17_01a-01", "09_01a-21", "01_01-13", "01_02c-18", "06_01-22", "08_01-12", "08_02-13", "10_01-14", "03_02-03", "16_01a-21", "05_01-03", "06_01-04", "06_01-16", "13_02-01", "07_02-16", "11_02-11", "14_01-09", "11_02c-16", "05_02-18", "14_01-13", "02_01-07", "17_01b-02", "01_01-18", "07_02-18", "01_02a-14", "14_01a-14", "11_02c-19", "17_01b-16", "03_01-09", "10_02-10", "14_01a-17", "03_01-02", "14_01b-04", "16_01a-10", "02_02-09", "17_01a-15", "05_02-10", "03_01-14", "10_01-17", "09_02-11", "09_02c-12", "01_02a-10", "03_01-16", "09_02c-05", "10_01-08", "17_01b-07", "08_01-18", "01_02b-06", "13_02-02", "01_01-12", "02_01-22", "14_01a-02", "09_01b-10", "07_01-09", "01_01-22", "09_01b-12", "07_02-13", "09_01b-22", "10_01-19", "10_01-07", "05_02-20", "08_01-17", "09_02c-10", "17_01b-17", "09_01a-13", "17_01a-22", "10_02c-21", "15_01a-18", "16_01b-14", "03_01-18", "08_02-19", "06_01-07", "02_01-16", "14_01b-17", "17_01a-16", "09_01-14", "11_02c-05", "07_02-05", "14_01-12", "05_02-09", "15_01b-11", "14_01-07", "01_02-17", "15_01a-07", "01_02a-16", "13_01-03", "10_01-04", "09_02-19", "16_01b-11", "09_01-05", "14_01-18", "05_01-02", "15_01a-23", "09_02-21", "09_01a-09", "10_02c-16", "17_01a-20", "17_01a-09", "07_02-19", "07_01-02", "01_02-10", "10_02-16", "03_01-10", "05_01c-12", "11_02-08", "11_02c-18", "08_01-16", "08_01-09", "11_01-13", "10_02-18", "09_02c-14", "09_02-03", "05_02-11", "13_01-05", "01_02c-05", "14_01b-22", "14_01-06", "17_01b-09", "10_02c-14", "16_01a-06", "01_02a-12", "11_02-18", "11_02c-12", "14_01b-08", "07_01-20", "14_02-05", "03_02-11", "07_02-15", "01_01-10", "10_01-03", "09_02-23", "01_02a-06", "17_01a-23", "11_01-23", "15_01b-19", "11_02-01", "17_01a-04", "14_01-19", "10_02-03", "09_01a-08", "09_02-01", "05_01-20", "13_01-13", "07_01-01", "04_01-20", "14_01a-09", "05_02-01", "03_02-01", "08_02-21", "01_02-06", "11_01-20", "03_01-06", "16_01b-17", "09_01b-13", "08_01-04", "05_02-06", "13_01-19", "09_01-02", "06_01-15", "01_02b-13", "14_01b-16", "02_01-04", "08_01-05", "01_01-06", "11_02c-09", "03_02-17", "01_02b-23", "08_02-16", "10_02c-18", "07_01-16", "11_01-16", "01_02b-18", "11_02-07", "14_01b-09", "09_02c-03", "03_01-12", "09_01a-07", "05_01-17", "04_01-10", "13_02-08", "07_02-01", "09_02-08", "05_01c-13", "16_01b-02", "02_02-18", "09_01b-19", "09_02c-09", "14_01-05", "14_01b-12", "05_01c-06", "08_02-07", "09_01b-20", "05_01-10", "05_01-11", "13_01-02", "16_01b-19", "04_01-14", "13_02-14", "14_01a-04", "07_02-23", "09_01-06", "04_01-15", "01_02c-13", "16_01b-03", "15_01a-16", "02_01-05", "14_01a-07", "08_01-11", "04_01-17", "14_01-20", "05_01-22", "09_01a-17", "09_01b-04", "09_01-15", "15_01a-13", "02_02-04", "14_01a-19", "09_01a-23", "07_01-15", "14_01a-23", "16_01b-05", "07_02-14", "08_02-22", "14_01-11", "02_02-06", "05_02-15", "15_01a-19", "11_01-02", "13_02-10", "01_02-02", "10_01-15", "14_01-01", "01_02c-09", "07_01-14", "03_02-20", "05_01c-01", "06_01-10", "09_01-21", "15_01a-01", "10_02-09", "11_02c-15", "02_01-17", "14_02-10", "01_02-22", "01_02c-16", "14_01b-23", "16_01a-04", "16_01b-22", "10_02c-03", "14_01a-12", "15_01a-11", "09_01a-03", "11_01-15", "09_01a-15", "16_01a-17", "17_01b-22", "07_02-03", "01_02b-05", "02_01-11", "16_01a-03", "03_01-11", "01_02b-07", "13_02-17", "03_02-12", "01_02c-11", "03_02-07", "17_01b-13", "09_02c-23", "02_02-23", "11_02c-20", "09_01b-14", "01_01-02", "09_02c-16", "02_02-11", "04_01-08", "02_01-01", "05_01c-08", "02_02-02", "01_02-19", "14_01a-18", "16_01a-16", "07_02-02", "04_01-09", "16_01b-12", "05_01-13", "08_02-18", "10_01-02", "01_02a-23", "10_01-12", "17_01a-08", "05_01c-09", "11_02-04", "01_02-01", "11_02-22", "17_01b-23", "05_01c-23", "09_02-12", "14_01b-15", "02_01-12", "13_01-22", "13_01-17", "08_01-13", "17_01b-04", "14_01a-16", "14_01b-10", "06_01-18", "02_02-07", "01_01-07", "07_02-09", "15_01a-15", "14_02-14", "10_02-13", "02_01-19", "13_02-11", "01_02-16", "14_01-21", "05_02-08", "14_01a-10", "14_01a-01", "17_01b-19", "15_01a-04", "01_02c-08", "08_01-21", "01_01-09", "13_02-18", "05_01-07", "11_02c-04", "16_01b-10", "15_01a-08", "17_01a-10", "10_01-18", "09_02c-17", "01_01-05", "05_01-12", "08_02-17", "02_01-14", "09_02-17", "01_01-16", "09_02c-13", "16_01a-19", "10_02-06", "09_01-20", "03_01-05", "10_01-21", "09_01-16", "07_02-12", "01_02c-19", "09_01b-02", "09_02c-08", "16_01a-13", "01_01-21", "01_02c-14", "03_02-19", "03_01-20", "10_02c-08", "13_02-03", "17_01a-03", "09_02-10", "14_01a-06", "09_02-09", "15_01a-06", "08_01-20", "14_01a-15", "01_02b-01", "01_02c-06", "15_01b-06", "14_02-09", "09_02c-02", "02_02-15", "11_02c-17", "05_02-04", "09_01b-11", "08_02-12", "09_02-13", "01_02-07", "01_02a-08", "01_02-11", "02_02-16", "04_01-19", "11_01-03", "14_02-18", "15_01b-01", "04_01-07", "14_02-12", "07_02-10", "14_01b-01", "04_01-21", "01_02b-21", "17_01b-03", "02_01-10", "08_02-04", "05_02-05", "17_01a-18", "13_01-11", "14_01b-20", "11_02c-01", "11_01-01", "10_02c-22", "02_01-20", "07_01-07", "11_02-12", "09_02c-01", "10_02-12", "11_01-07", "05_02-14", "17_01a-06", "10_02c-23", "01_01-08", "09_01a-14", "14_01-03", "11_02c-14", "02_02-03", "10_02-20", "16_01b-13", "14_01b-05", "09_01-13", "17_01b-20", "16_01a-18", "16_01a-23", "05_01c-07", "01_01-14", "14_02-02", "09_02c-19", "01_02c-02", "14_01-22", "01_02-14", "17_01b-06", "07_01-12", "03_01-01", "10_01-22", "02_02-17", "14_02-07", "10_02-05", "11_02-15", "09_02c-07", "10_02c-13", "05_02-13", "10_02c-20", "07_01-21", "11_02-06", "11_01-17", "14_02-22", "07_02-17", "05_01-14", "04_01-02", "08_02-02", "05_01c-04", "08_01-06", "01_01-04", "01_01-23", "09_01b-17", "09_01b-23", "08_01-01", "10_02-15", "03_01-07", "04_01-04", "17_01b-15", "01_02b-08", "15_01b-13", "08_01-15", "14_01b-19", "15_01b-03", "01_02-05", "10_01-05", "03_02-23", "09_02-22", "03_02-04", "01_02b-03", "11_02-05", "14_02-15", "01_02b-15", "09_02-02", "09_01-18", "02_02-22", "09_01-08", "08_02-06", "14_02-20", "01_02a-21", "03_01-03", "05_01-18", "11_01-19", "01_02-21", "16_01a-20", "15_01a-02", "14_01-14", "07_02-04", "14_01b-18", "16_01a-12", "09_02c-04", "16_01b-18", "06_01-14", "05_01c-17", "01_02b-04", "11_02-17", "09_02-15", "14_01b-14", "14_01b-06", "05_02-12", "09_01b-18", "11_02-21", "04_01-11", "15_01b-04", "07_02-22", "03_02-05", "02_01-08", "11_02c-08", "05_01c-22", "10_02-07", "17_01b-10", "14_01-04", "05_01c-05", "01_02a-20", "08_01-23", "01_02a-03", "16_01b-01", "10_02-19", "11_01-21", "01_02c-20", "09_02-20", "05_01c-02", "09_01b-15", "13_01-10", "09_02c-21", "09_01b-21", "09_02c-22", "15_01b-17", "06_01-21", "05_01-06", "10_01-20", "01_01-01", "14_01a-21", "17_01b-01", "05_01-19", "11_02-19", "16_01b-08", "14_02-06", "14_02-08", "11_01-12", "02_01-06", "02_02-21", "05_01c-10", "10_02c-09", "13_02-12", "11_01-05", "09_02c-20", "01_02-18", "14_02-11", "02_01-23", "17_01a-05", "11_01-06", "11_02-02", "02_02-13", "17_01a-11", "06_01-06", "17_01a-21", "01_02c-21", "09_02-16", "11_02-13", "05_01-21", "13_01-01", "10_02c-10", "14_01b-03", "13_02-06", "04_01-22", "11_02c-23", "09_01-04", "05_01-16", "13_01-08", "09_02c-18", "09_01a-10", "09_01b-06", "03_01-17", "13_02-19", "01_02c-22", "11_01-11", "13_01-06", "15_01b-15", "13_01-15", "09_02-06", "09_01b-08", "03_02-18", "17_01b-08", "15_01a-17", "01_02b-12", "01_02a-09", "05_01-05", "04_01-06", "09_01-12", "14_01b-02", "03_01-15", "14_01a-11", "03_02-22", "15_01a-05", "09_01a-01", "01_02a-01", "01_02-23", "14_01-08", "08_01-19", "14_01b-13", "06_01-03", "13_01-16", "09_01b-09", "14_02-13", "01_02c-01", "03_01-08", "10_02c-17", "08_02-08", "13_01-09", "16_01a-15", "14_01b-21", "02_01-18", "01_02b-14", "05_01c-14", "04_01-05", "02_01-09", "11_02-16", "15_01a-12", "13_02-05", "14_01-10", "16_01a-09", "16_01b-06", "17_01a-12", "15_01b-16", "09_01a-06", "14_02-01", "02_01-15", "16_01a-11", "13_02-04", "05_01c-03", "01_02c-23", "13_02-16", "09_01b-03", "05_01-15", "11_01-22", "10_02c-06", "11_01-09", "16_01a-08", "14_01-17", "13_02-15", "09_01-11", "09_02c-15", "14_01a-05", "01_02a-05", "06_01-12", "08_02-23", "14_01-15", "10_02-14", "08_01-10", "17_01b-12", "16_01b-09", "10_02-04", "13_01-18", "02_01-13", "09_01a-18", "09_01b-16", "07_01-11", "09_02-07", "16_01b-21", "16_01b-20", "09_01-01", "09_01a-20", "05_01-09", "01_02a-19", "06_01-08", "09_01-10", "05_01c-18", "01_02b-19", "11_02c-11", "06_01-01", "01_01-15", "05_02-16", "02_02-10", "10_02c-12", "04_01-16", "01_02b-10", "01_01-19", "02_02-12", "15_01b-22", "07_01-05", "10_01-06", "11_02c-06", "10_02c-19", "09_01-07", "10_01-11", "13_02-22", "11_01-10", "03_02-09", "08_01-14", "06_01-20", "09_01a-12", "08_02-09", "10_02c-11", "01_02-08", "11_01-18", "02_02-19", "01_02a-18", "17_01a-19", "17_01a-14", "14_02-19", "08_02-05", "09_01a-04", "07_01-06", "01_02a-04", "10_02-08", "09_01-19", "13_02-21", "05_01c-16", "15_01b-14", "01_01-20", "03_02-14", "17_01a-02", "16_01a-05", "09_02-14", "05_01c-19", "05_01-04", "04_01-01", "09_01-03", "10_02c-15", "11_02c-13", "16_01b-07", "16_01b-15", "07_01-18", "08_02-15", "09_01a-05", "17_01b-21", "01_02c-12", "15_01a-03", "11_02-03", "09_01a-11", "06_01-17", "01_02b-16", "15_01b-10", "01_02-12", "14_02-03", "07_02-20", "17_01a-17", "01_02b-17", "07_01-22", "14_01b-07", "16_01a-07", "15_01a-22", "05_02-03", "03_02-06", "13_01-12", "01_02c-04", "08_02-14", "15_01a-10", "06_01-05", "01_02a-02", "03_02-02", "02_02-14", "11_02c-10", "15_01a-20", "14_01b-11", "01_02a-22", "08_01-02", "01_02c-15", "15_01b-02", "15_01b-18", "13_02-07", "11_01-08", "09_02-18", "17_01b-05", "07_01-08"]
valIds = ["09_01b-05", "10_02c-01", "07_01-17", "17_01a-07", "05_01c-20", "16_01b-16", "01_02c-07", "14_02-17", "05_02-07", "13_02-13", "07_02-07", "08_02-20", "14_02-16", "01_02b-11", "03_01-13", "03_02-10", "10_02-02", "09_02-05", "05_02-17", "01_02-15", "14_02-21", "02_01-21", "02_02-08", "14_01-02", "08_02-03", "14_01a-22", "07_01-04", "10_02c-07", "02_02-05", "02_01-03", "02_02-20", "01_02-03", "09_01-09", "04_01-13", "06_01-02", "13_01-21", "11_02-20", "13_01-04", "01_02-04", "10_02-01", "11_02c-21", "16_01a-01", "01_02a-07", "10_02-11", "09_01-22", "05_02-19", "03_02-21", "09_01-17", "08_02-01", "10_01-10", "07_02-21", "10_01-13", "01_02-20", "13_01-07", "13_02-09", "07_01-03", "10_02c-05", "10_02-22", "01_01-03", "13_02-20", "15_01b-20", "11_02-09", "15_01b-21", "11_02c-07", "15_01a-14", "05_02-22", "09_01a-22", "17_01b-11", "10_01-09", "11_01-14", "05_01c-21", "01_02-13", "01_02b-22", "08_02-11", "14_01a-08", "02_01-02", "08_01-08", "03_02-15", "01_02b-09", "01_02a-13", "11_01-04", "13_01-14", "07_01-13", "15_01b-23", "01_02c-17", "15_01b-08", "14_01a-13", "03_01-04", "14_01a-03", "07_01-10", "16_01a-22", "05_01-01", "07_02-08", "09_01a-19", "10_02c-04", "06_01-09", "17_01b-18", "11_02-10", "09_02c-06", "11_02c-02", "05_01c-15", "04_01-03", "07_02-06", "17_01b-14", "16_01a-02", "04_01-12", "08_01-22", "02_02-01", "09_01a-02", "15_01b-12", "01_01-17", "16_01b-04", "15_01b-07", "06_01-11", "15_01b-09", "04_01-18", "05_01-08", "13_01-20", "16_01a-14", "03_02-08", "15_01a-09", "14_01-16", "10_02c-02", "09_01b-07", "10_02-21", "05_02-02", "09_02-04", "08_02-10", "09_01b-01", "03_02-16", "10_01-01", "01_02-09", "11_02-14", "14_01a-20", "01_02a-11", "01_02b-02", "08_01-03", "01_02c-03", "03_02-13"]
testIds = ["12_01-01","12_01-02","12_01-03","12_01-04","12_01-05","12_01-06","12_01-07","12_01-08","12_01-09","12_01-10", "12_01-11","12_01-12","12_01-13","12_01-14","12_01-15","12_01-16","12_01-17","12_01-18","12_01-19","12_01-20","12_01-21","12_01-22","12_01-23","12_01a-01","12_01a-02","12_01a-03","12_01a-04","12_01a-05","12_01a-06","12_01a-07","12_01a-08","12_01a-09","12_01a-10", "12_01a-11","12_01a-12","12_01a-13","12_01a-14","12_01a-15","12_01a-16","12_01a-17","12_01a-18","12_01a-19","12_01a-20","12_01a-21","12_01a-22","12_01a-23","12_01b-01","12_01b-02","12_01b-03","12_01b-04","12_01b-05","12_01b-06","12_01b-07","12_01b-08","12_01b-09","12_01b-10", "12_01b-11","12_01b-12","12_01b-13","12_01b-14","12_01b-15","12_01b-16","12_01b-17","12_01b-18","12_01b-19","12_01b-20","12_01b-21","12_01b-22","12_01b-23","12_02-01","12_02-02","12_02-03","12_02-04","12_02-05","12_02-06","12_02-07","12_02-08","12_02-09","12_02-10", "12_02-11","12_02-12","12_02-13","12_02-14","12_02-15","12_02-16","12_02-17","12_02-18","12_02-19","12_02-20","12_02-21","12_02-22","18_01a-01","18_01a-02","18_01a-03","18_01a-04","18_01a-05","18_01a-06","18_01a-07","18_01a-08","18_01a-09","18_01a-10", "18_01a-11","18_01a-12","18_01a-13","18_01a-14","18_01a-15","18_01a-16","18_01a-17","18_01a-18","18_01a-19","18_01a-20","18_01a-21","18_01a-22","18_01a-23","18_01b-01","18_01b-02","18_01b-03","18_01b-04","18_01b-05","18_01b-06","18_01b-07","18_01b-08","18_01b-09","18_01b-10", "18_01b-11","18_01b-12","18_01b-13","18_01b-14","18_01b-15","18_01b-16","18_01b-17","18_01b-18","18_01b-19","18_01b-20","18_01b-21","18_01b-22","18_01b-23"]

#read the train, test ,valid ids from file
# mainPath = './Parsers/IzaDataToChartText/'
# trainPath = mainPath + 'ids_train_a.txt'
# valPath = mainPath + 'ids_val_a.txt'
# testPath = mainPath + 'ids_test_a.txt'

# trainIds = openCaption(trainPath)
# valIds = openCaption(valPath)
# testIds = openCaption(testPath)

idx = 1
for m in range(len(trainIds)):
    id = trainIds[m]
    topic_id = id.split('_')[0]
    
    chart = id.split('_')[1]
    chart_id = chart.split('-')[0]

    summary_id =  chart.split('-')[1]
    if(int(summary_id) < 10):
        summary_id = summary_id[1]
    summary_id = summary_id.strip()

    dataPath = './Parsers/IzaDataToChartText/structured_chart_iza_data/' + str(topic_id) + '/' + str(chart_id) + '/data.csv' 
    captionPath = './Parsers/IzaDataToChartText/structured_chart_iza_data/' + str(topic_id) + '/' + str(chart_id) + '/' + str(summary_id) + '.txt'
    titlePath = './Parsers/IzaDataToChartText/structured_chart_iza_data/' + str(topic_id) + '/' + str(chart_id) + '/title.txt'

    targetDataPath = './Parsers/IzaDataToChartText/combined_iza_salman_data/data/' + str(idx) + '.csv'
    targetCaptionPath = './Parsers/IzaDataToChartText/combined_iza_salman_data/captions/' + str(idx) + '.txt'
    targetTitlePath = './Parsers/IzaDataToChartText/combined_iza_salman_data/titles/' + str(idx) + '.txt'

    shutil.copyfile(dataPath, targetDataPath)
    shutil.copyfile(captionPath, targetCaptionPath)
    shutil.copyfile(titlePath, targetTitlePath)

    idx = idx+1

for m in range(len(valIds)):
    id = valIds[m]
    topic_id = id.split('_')[0]
    
    chart = id.split('_')[1]
    chart_id = chart.split('-')[0]

    summary_id =  chart.split('-')[1]
    if(int(summary_id) < 10):
        summary_id = summary_id[1]
    summary_id = summary_id.strip()


    dataPath = './Parsers/IzaDataToChartText/structured_chart_iza_data/' + str(topic_id) + '/' + str(chart_id) + '/data.csv' 
    captionPath = './Parsers/IzaDataToChartText/structured_chart_iza_data/' + str(topic_id) + '/' + str(chart_id) + '/' + str(summary_id) + '.txt'
    titlePath = './Parsers/IzaDataToChartText/structured_chart_iza_data/' + str(topic_id) + '/' + str(chart_id) + '/title.txt'

    targetDataPath = './Parsers/IzaDataToChartText/combined_iza_salman_data/data/' + str(idx) + '.csv'
    targetCaptionPath = './Parsers/IzaDataToChartText/combined_iza_salman_data/captions/' + str(idx) + '.txt'
    targetTitlePath = './Parsers/IzaDataToChartText/combined_iza_salman_data/titles/' + str(idx) + '.txt'

    shutil.copyfile(dataPath, targetDataPath)
    shutil.copyfile(captionPath, targetCaptionPath)
    shutil.copyfile(titlePath, targetTitlePath)

    idx = idx+1

for m in range(len(testIds)):
    id = testIds[m]
    topic_id = id.split('_')[0]
    
    chart = id.split('_')[1]
    chart_id = chart.split('-')[0]

    summary_id =  chart.split('-')[1]
    if(int(summary_id) < 10):
        summary_id = summary_id[1]
    summary_id = summary_id.strip()


    dataPath = './Parsers/IzaDataToChartText/structured_chart_iza_data/' + str(topic_id) + '/' + str(chart_id) + '/data.csv' 
    captionPath = './Parsers/IzaDataToChartText/structured_chart_iza_data/' + str(topic_id) + '/' + str(chart_id) + '/' + str(summary_id) + '.txt'
    titlePath = './Parsers/IzaDataToChartText/structured_chart_iza_data/' + str(topic_id) + '/' + str(chart_id) + '/title.txt'

    targetDataPath = './Parsers/IzaDataToChartText/combined_iza_salman_data/data/' + str(idx) + '.csv'
    targetCaptionPath = './Parsers/IzaDataToChartText/combined_iza_salman_data/captions/' + str(idx) + '.txt'
    targetTitlePath = './Parsers/IzaDataToChartText/combined_iza_salman_data/titles/' + str(idx) + '.txt'

    shutil.copyfile(dataPath, targetDataPath)
    shutil.copyfile(captionPath, targetCaptionPath)
    shutil.copyfile(titlePath, targetTitlePath)

    idx = idx+1
print(len(trainIds), len(valIds), len(testIds))
#### Iza shuffle ends


#### This is to shuffle chart2text bar chart data #####

# mainPath = './dataset_barchart/'
# dataPath = mainPath + 'data.txt'
# captionPath = mainPath + 'OriginalSummary.txt'
# titlePath = mainPath + 'titles.txt'

# data = openCaption(dataPath)
# captions = openCaption(captionPath)
# titles = openCaption(titlePath)

# print(len(data), len(captions), len(titles))
# assert(len(data) == len(captions) == len(titles))

# data, captions, titles = utils.shuffle(data, captions, titles, random_state=0)

# with open('./dataset_barchart/data_shuffled.txt', mode='wt', encoding='utf8') as myfile1:
#     myfile1.writelines("%s" % line for line in data)

# with open('./dataset_barchart/OriginalSummary_shuffled.txt', mode='wt', encoding='utf8') as myfile1:
#     myfile1.writelines("%s" % line for line in captions)

# with open('./dataset_barchart/titles_shuffled.txt', mode='wt', encoding='utf8') as myfile1:
#     myfile1.writelines("%s" % line for line in titles)
####shuffle end #######


#### This is to shuffle chart2text Data in folder structure
# dataFiles = os.listdir('./dataset_barchart//data')
# dataFiles.sort()
# # dataFiles = dataFiles[0:2]

# captionFiles = os.listdir('./dataset_barchart/captions')
# captionFiles.sort()
# # captionFiles = captionFiles[0:2]

# titleFiles = os.listdir('./dataset_barchart/titles')
# titleFiles.sort()
# # titleFiles = titleFiles[0:2]

# assert len(captionFiles) == len(dataFiles) == len(titleFiles)
# print(len(captionFiles), len(dataFiles), len(titleFiles))
# # print(titleFiles)

# dataFiles, captionFiles, titleFiles = utils.shuffle(dataFiles, captionFiles, titleFiles, random_state=0)

# idx = 1
# for m in range(len(dataFiles)):
#     dataPath = './dataset_barchart/data/' + dataFiles[m]
#     captionPath = './dataset_barchart/captions/' + captionFiles[m]
#     titlePath = './dataset_barchart/titles/' + titleFiles[m]

#     targetDataPath = './dataset_barchart/shuffled_data/' + str(idx) + '.csv'
#     targetCaptionPath = './dataset_barchart/shuffled_captions/' + str(idx) + '.txt'
#     targetTitlePath = './dataset_barchart/shuffled_titles/' + str(idx) + '.txt'

#     shutil.copyfile(dataPath, targetDataPath)
#     shutil.copyfile(captionPath, targetCaptionPath)
#     shutil.copyfile(titlePath, targetTitlePath)

#     idx = idx+1
#### shuffle ends