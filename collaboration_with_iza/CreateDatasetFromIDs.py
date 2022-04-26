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

mainSourcePath = '../Chart2TextCodeExtraction/Parsers/IzaDataToChartText/structured_chart_iza_data/'
mainTargetPath = './additional_data/dataset/mixed/'

with open('./additional_data/splits_combinations_ids.json') as json_file:
    json_chart_data = json.load(json_file)

with open('./additional_data/chartID2additional_info_salman.json') as json_file:
    additional_info = json.load(json_file)

trainIds = json_chart_data['mixed']['train']
valIds = json_chart_data['mixed']['val']
testIds = json_chart_data['mixed']['test']

# print(trainIds)
print(len(trainIds), len(valIds), len(testIds))

data_table = []

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

    pipe_separated_data_table = ""
    id_for_additional_info = id.split('-')[0]
    items = additional_info[id_for_additional_info].items()
    for key,value in items:
        key = key.replace(" ", "_")
        value = value.replace(" ", "_")
        if(value.isnumeric()):
            pipe_separated_data_table += 'Relation' + '|' + str(key) + '|' + 'y2' + '|' + 'bar_chart' + " "
            pipe_separated_data_table += 'Relation' + '|' + str(value) + '|' + 'y2' + '|' + 'bar_chart' + " "
        else:
            pipe_separated_data_table += 'Relation' + '|' + str(key) + '|' + 'x2' + '|' + 'bar_chart' + " "
            pipe_separated_data_table += 'Relation' + '|' + str(value) + '|' + 'x2' + '|' + 'bar_chart' + " "

    data_table.append(pipe_separated_data_table)


    dataPath = mainSourcePath + str(topic_id) + '/' + str(chart_id) + '/data.csv' 
    captionPath = mainSourcePath + str(topic_id) + '/' + str(chart_id) + '/' + str(summary_id) + '.txt'
    titlePath = mainSourcePath + str(topic_id) + '/' + str(chart_id) + '/title.txt'

    targetDataPath = mainTargetPath + 'data/' + str(idx) + '.csv'
    targetCaptionPath = mainTargetPath + 'captions/' + str(idx) + '.txt'
    targetTitlePath = mainTargetPath + 'titles/' + str(idx) + '.txt'

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

    pipe_separated_data_table = ""
    id_for_additional_info = id.split('-')[0]
    items = additional_info[id_for_additional_info].items()
    for key,value in items:
        key = key.replace(" ", "_")
        value = value.replace(" ", "_")

        if(value.isnumeric()):
            pipe_separated_data_table += 'Relation' + '|' + str(key) + '|' + 'x2' + '|' + 'bar_chart' + " "
            pipe_separated_data_table += 'Relation' + '|' + str(value) + '|' + 'x2' + '|' + 'bar_chart' + " "
        else:
            pipe_separated_data_table += 'Relation' + '|' + str(key) + '|' + 'y2' + '|' + 'bar_chart' + " "
            pipe_separated_data_table += 'Relation' + '|' + str(value) + '|' + 'y2' + '|' + 'bar_chart' + " "

    data_table.append(pipe_separated_data_table)

    dataPath = mainSourcePath + str(topic_id) + '/' + str(chart_id) + '/data.csv' 
    captionPath = mainSourcePath + str(topic_id) + '/' + str(chart_id) + '/' + str(summary_id) + '.txt'
    titlePath = mainSourcePath + str(topic_id) + '/' + str(chart_id) + '/title.txt'

    targetDataPath = mainTargetPath + 'data/' + str(idx) + '.csv'
    targetCaptionPath = mainTargetPath + 'captions/' + str(idx) + '.txt'
    targetTitlePath = mainTargetPath + 'titles/' + str(idx) + '.txt'

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

    pipe_separated_data_table = ""
    id_for_additional_info = id.split('-')[0]
    items = additional_info[id_for_additional_info].items()
    for key,value in items:
        key = key.replace(" ", "_")
        value = value.replace(" ", "_")
        
        if(value.isnumeric()):
            pipe_separated_data_table += 'Relation' + '|' + str(key) + '|' + 'x2' + '|' + 'bar_chart' + " "
            pipe_separated_data_table += 'Relation' + '|' + str(value) + '|' + 'x2' + '|' + 'bar_chart' + " "
        else:
            pipe_separated_data_table += 'Relation' + '|' + str(key) + '|' + 'y2' + '|' + 'bar_chart' + " "
            pipe_separated_data_table += 'Relation' + '|' + str(value) + '|' + 'y2' + '|' + 'bar_chart' + " "

    data_table.append(pipe_separated_data_table)

    dataPath = mainSourcePath + str(topic_id) + '/' + str(chart_id) + '/data.csv' 
    captionPath = mainSourcePath + str(topic_id) + '/' + str(chart_id) + '/' + str(summary_id) + '.txt'
    titlePath = mainSourcePath + str(topic_id) + '/' + str(chart_id) + '/title.txt'

    targetDataPath = mainTargetPath + 'data/' + str(idx) + '.csv'
    targetCaptionPath = mainTargetPath + 'captions/' + str(idx) + '.txt'
    targetTitlePath = mainTargetPath + 'titles/' + str(idx) + '.txt'

    shutil.copyfile(dataPath, targetDataPath)
    shutil.copyfile(captionPath, targetCaptionPath)
    shutil.copyfile(titlePath, targetTitlePath)

    idx = idx+1


with open(mainTargetPath + "relations.txt", "w") as data_file:
    for data in data_table:
        data_file.write(data + "\n")