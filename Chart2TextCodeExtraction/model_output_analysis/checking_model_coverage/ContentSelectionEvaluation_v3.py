# this file calculates the content selection part 3 of the model. Content Selection v3 is calculated by how much of the template_variables from the chart data (title, axis names, x/y bar values) are there in the generated summary.

from statistics import mean, stdev
from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance
import pandas as pd


# mainPath = './NewIzaData vs OldIzaData/'


# generatedWithoutTemplatePath = mainPath + 'NewGenerated.txt'
# dataPath = mainPath + 'NewTestData.txt'
# titlePath = mainPath + 'NewTestTitle.txt'

# Path for testing in the folder "collaboration with iza"
mainPath = '../../../collaboration_with_iza/models/train_iza-unseen-c2t_test_iza-unseen_new/'

generatedWithoutTemplatePath = mainPath + 'results/aug17/generated-p80.txt'
dataPath = mainPath + 'data/test/testData.txt'
titlePath = mainPath + 'data/test/testTitle.txt'


fillers = ['in', 'the', 'and', 'or', 'an', 'as', 'can', 'be', 'a', ':', '-',
           'to', 'but', 'is', 'of', 'it', 'on', '.', 'at', '(', ')', ',', ';']



stringMatchingThreshold = 0.85

generatedScores = []
baselineScores = []
untemplatedScores = []

with  open(generatedWithoutTemplatePath, 'r', encoding='utf-8') as generatedWithoutTemplateFile, \
        open(titlePath, 'r', encoding='utf-8') as titleFile, \
            open(dataPath, 'r', encoding='utf-8') as dataFile:
    for generatedWithoutTemplate, title, data in zip(generatedWithoutTemplateFile.readlines(), titleFile.readlines(), dataFile.readlines()):
        generatedWithoutTemplatesArr = generatedWithoutTemplate.split()
        titleArr = title.split()
        dataArr = data.split()

        recordList = []

        for titl in titleArr:
            if(titl.lower() not in fillers and titl.lower() not in recordList):
                recordList.append(titl.lower())

        dat0 = dataArr[0]
        dat1 = dataArr[1]
        xAxisName = dat0.split('|')[0]
        yAxisName = dat1.split('|')[0]

        xAxisName = xAxisName.split('_')
        for x in xAxisName:
            if(x.lower() not in fillers and x.lower() not in recordList):
                recordList.append(x.lower())

        yAxisName = yAxisName.split('_')
        for y in yAxisName:
            if(y.lower() not in fillers and y.lower() not in recordList):
                recordList.append(y.lower())
            
        
        for dat in dataArr:
            dat = dat.split('|')
            if(dat[1].lower() not in fillers and dat[1].lower() not in recordList):
                recordList.append(dat[1].lower())

        list1 = recordList
        recordLength = len(recordList)
        generatedList = []
        for token in generatedWithoutTemplatesArr:
            for word in list1:
                if token.lower() == word:
                    list1.remove(word)
                    generatedList.append(word)
                    break
      
        generatedRatio = len(generatedList) / recordLength
        generatedScores.append(generatedRatio)


print(f'generated CS stdev: {round(stdev(generatedScores)*100,2)}%')
print()
print(f'generated CS mean: {round(mean(generatedScores)*100,2)}%')
print()
print(f'generated CS RSD: {round((stdev(generatedScores)*100) / abs(mean(generatedScores)),2)}%')

