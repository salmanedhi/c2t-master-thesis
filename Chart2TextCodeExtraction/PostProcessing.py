## this file contains the post processing step
import spacy
import en_core_web_md
import re
import pandas as pd
from fitbert.fitb import FitBert

def openData(path):
    with open(path, 'r', encoding='utf-8') as captionFile:
        data = captionFile.readlines()
    return data

def askBert(masked_string, options):
    ranked_options = fb.rank(masked_string, options)
    #print(ranked_options)
    return ranked_options[0]

def getNamedEntity(title, xValueArr):
    doc = nlp(title)
    entities = {}
    entities['Subject'] = []
    entities['Date'] = []
    for X in doc.ents:
        if X.label_ == 'GPE' or X.label_ == 'ORG' or X.label_ == 'NORP' or X.label_ == 'LOC':
            cleanSubject = [word for word in X.text.split() if word.isalpha() and word not in fillers]
            if len(cleanSubject) > 0:
                entities['Subject'].append(' '.join(cleanSubject))
        elif X.label_ == 'DATE':
            if X.text.isnumeric():
                entities['Date'].append(X.text)
    if len(entities['Subject']) == 0:
        uppercaseWords = [word for word in title.split() if word[0].isupper()]
        if len(uppercaseWords) > 1:
            guessedSubject = ' '.join(uppercaseWords[1:])
        else:
            guessedSubject = uppercaseWords[0]
        entities['Subject'].append(guessedSubject)
    if len(entities['Date']) == 0:
        if xLabel[0] == 'Month':
            years = []
            for item in xValueArr:
                [years.append(year.replace('\'', '')) for year in item.split('_') if year.replace('\'', '').isnumeric()]
            if len(years) > 0:
                entities['Date'] = [min(years), max(years)]
        elif xLabel[0] == 'Year':
            years = [year for year in title.split() if year.replace('/', '').isnumeric()]
            if len(years) > 0:
                entities['Date'] = [min(years), max(years)]
        else:
            try:
                years = [year for year in title.split() if year.isnumeric()]
                if len(years) > 0:
                    entities['Date'] = [min(years), max(years)]
            except:
                p = 0
    return entities

def are_numbers(stringList):
    try:
        for value in stringList:
            float(value)
        return True
    except ValueError:
        return False

#valueArr is the array of the idxmax/min (x or y)
#type is min/max
def mapParallelIndex(valueArr, type):
    if are_numbers(valueArr):
        try:
            array = [float(i) for i in valueArr]
            if type == 'max':
                index = array.index(max(array))
                return int(index)
            elif type == 'min':
                index = array.index(min(array))
                return int(index)
        except:
            print('Parallel num err')
            print(valueArr, type)
            return 0
    else:
        try:
            array = [float(i.split('_')[-1:][0]) for i in valueArr]
            if type == 'max':
                index = array.index(max(array))
                return int(index)
            elif type == 'min':
                index = array.index(min(array))
                return int(index)
        except:
            print('Parallel num err')
            print(valueArr, type)
            return 0


def getScale(title, xLabel, yLabel):
    #add Share
    for xLabelToken in xLabel:
        xLabelWord = xLabelToken.replace('_', ' ').lower()
        if xLabelWord in scales:
            return xLabelWord
    for yLabelToken in yLabel:
        yLabelWord = yLabelToken.replace('_', ' ').lower()
        if yLabelWord in scales:
            return yLabelWord
    for titleToken in title:
        if titleToken in scales:
            return titleToken
    return 'scaleError'


def mapIndex(index, array):
    if are_numbers(array):
        try:
            array = [float(i) for i in array]
            if str(index) == 'max':
                index = array.index(max(array))
                return int(index)
            elif str(index) == 'min':
                index = array.index(min(array))
                return int(index)
        except:
            print('numbers num err')
            return 0

    elif are_numbers(array[0:len(array) - 1]):
        try:
            array = [float(i) for i in array[0:len(array) - 1]]
            if str(index) == 'max':
                index = array.index(max(array))
                return int(index)
            elif str(index) == 'min':
                index = array.index(min(array))
                return int(index)
        except:
            print('n-1 num err')
            return 0

    if index == 'last':
        index = len(array) - 1
        return int(index)
    try:
        # this exception occurs with min/max on data which isn't purely numeric: ex. ['10_miles_or_less', '11_-_50_miles', '51_-_100_miles']
        cleanArr = [float("".join(filter(str.isdigit, item))) for item in array if
                    "".join(filter(str.isdigit, item)) != '']
        if str(index) == 'max':
            index = cleanArr.index(max(cleanArr))
            return int(index)
        elif str(index) == 'min':
            index = cleanArr.index(min(cleanArr))
            return int(index)
        return int(index)
    except:
        if not are_numbers(array) and (index == 'min' or index == 'max'):
            return 0
        return int(index)
def replaceTrends(reverse):
    tokens = reverse.split()
    if 'templatePositiveTrend' in tokens:
        while 'templatePositiveTrend' in tokens:
            index = tokens.index('templatePositiveTrend')
            tokens[index] = '***mask***'
            replacedToken = askBert(' '.join(tokens), positiveTrends)
            sentenceTemplates[index] = {'templatePositiveTrend' : replacedToken}
            tokens[index] = replacedToken
    if 'templateNegativeTrend' in tokens:
        while 'templateNegativeTrend' in tokens:
            index = tokens.index('templateNegativeTrend')
            tokens[index] = '***mask***'
            replacedToken = askBert(' '.join(tokens), negativeTrends)
            sentenceTemplates[index] = {'templateNegativeTrend':replacedToken}
            tokens[index] = replacedToken
    if 'scaleError' in tokens:
        while 'scaleError' in tokens:
            index = tokens.index('scaleError')
            tokens[index] = '***mask***'
            replacedToken = askBert(' '.join(tokens), scales)
            sentenceTemplates[index] = {'templateScale':replacedToken}
            tokens[index] = replacedToken
    newReverse = ' '.join(tokens)
    if newReverse[-2:] == '. ':
        return newReverse[:-2]
    elif '.' not in newReverse[-2:]:
        return newReverse + ' . '
    return newReverse

def getSubject(titleTokens, nerEntities):
    entities = {}
    entities['Subject'] = []
    entities['Date'] = []
    # manually find dates, it performs better than using NER
    for word in titleTokens:
        # if '2020' in word and word.isnumeric() and len(word) > 3:
        #     print(word)
        if word.isnumeric():
            if len(word) > 3: # can this be assumed that is is a date? >3 condition
                entities['Date'].append(word)        
        elif word.replace('/', '').isnumeric():
            word = word.split('/')[0]
            if len(word) > 3:
                entities['Date'].append(word)
        elif word.replace('-', '').isnumeric():
            word = word.split('-')[0]
            if len(word) > 3:
                entities['Date'].append(word)
    # get named entites from title
    for X in nerEntities:
        if X.label_ == 'GPE' or X.label_ == 'ORG' or X.label_ == 'NORP' or X.label_ == 'LOC':
            cleanSubject = [word for word in X.text.split() if word.isalpha() and word not in fillers]
            if len(cleanSubject) > 0:
                entities['Subject'].append(' '.join(cleanSubject))
        if len(entities['Date']) < 1:
            if X.label_ == 'DATE':
                if X.text.isnumeric():
                    entities['Date'].append(X.text)
    # guess subject if NER doesn't find one
    if len(entities['Subject']) == 0:
        uppercaseWords = [word for word in titleTokens if word[0].isupper()] #If the first letter of the word is uppercased, it is included as subject
        if len(uppercaseWords) > 1:
            guessedSubject = ' '.join(uppercaseWords[1:])
        else:
            guessedSubject = uppercaseWords[0]
        entities['Subject'].append(guessedSubject)
    # print(entities['Date'])
    cleanTitle = [titleWord for titleWord in titleTokens if titleWord.lower() not in fillers]
    return entities, cleanTitle

nlp = spacy.load('en_core_web_md')
fb = FitBert()

#def main():
scales = ['percent', 'percentage', '%', 'hundred', 'thousand', 'million', 'billion', 'trillion',
              'hundreds', 'thousands', 'millions', 'billions', 'trillions']
positiveTrends = ['increased', 'increase', 'increasing', 'grew', 'growing', 'rose', 'rising', 'gained', 'gaining']
negativeTrends = ['decreased', 'decrease', 'decreasing', 'shrank', 'shrinking', 'fell', 'falling', 'dropped',
                  'dropping']
fillers = ['in', 'the', 'and', 'or', 'an', 'as', 'can', 'be', 'a', ':', '-',
           'to', 'but', 'is', 'of', 'it', 'on', '.', 'at', '(', ')', ',', ';']


dataPath = './dataset_barchart/data.txt'
summaryPath = './dataset_barchart/PreProcesssedStringComparisionSummary.txt'
titlePath = './dataset_barchart/titles.txt'

dataList = openData(dataPath)
# data = data[1]

generatedList = openData(summaryPath)
# generated = generated[1]

titleList = openData(titlePath)
# title = title[1]

finalSentences = []

assert len(dataList) == len(generatedList) == len(titleList)
print(len(titleList))
for k in range(len(titleList)):

    data = dataList[k]
    generated = generatedList[k]
    title = titleList[k]

    datum = data.split()
    templateList = []

    xValueArr = []
    yValueArr = []
    cleanXArr = []
    cleanYArr = []
    xLabel = datum[0].split('|')[0].split('_')
    yLabel = datum[1].split('|')[0].split('_')
    chartType = datum[0].split('|')[3].split('_')[0]
    # remove filler words from labels
    cleanXLabel = [xWord for xWord in xLabel if xWord.lower() not in fillers]
    cleanYLabel = [yWord for yWord in yLabel if yWord.lower() not in fillers]

    for j in range(0, len(datum)):
        if j % 2 == 0:
            xValueArr.append(datum[j].split('|')[1])
            cleanXArr.append(datum[j].split('|')[1].replace('_', ' '))
        else:
            yValueArr.append(datum[j].split('|')[1])
            cleanYArr.append(datum[j].split('|')[1].replace('_', ' '))

    sentences = generated.split(' . ')

    doc = nlp(title)
    entities, cleanTitle = getSubject(title.split(), doc.ents)
    # entities = getNamedEntity(title, xValueArr)
    # print("title: ", title)
    # print("entities: ", entities)
    titleArr = [word for word in title.split() if word.lower() not in fillers]
    reversedSentences = []

    for sentence in sentences:
        tokens = sentence.split()
        sentenceTemplates = {}
        reversedTokens = []
        for token, i in zip(tokens, range(0, len(tokens))):
            templateAxis = ''
            if i < (len(tokens) - 1):
                if tokens[i] == tokens[i + 1]:
                    print(f'1:{tokens[i]} 2:{tokens[i + 1]}')
                    print(f'popped: {tokens[i + 1]}')
                    print('k ' , k)
                    exit()
                    tokens.pop(i + 1)
            if 'template' in token and 'Trend' not in token:
                if 'idxmax' in token or 'idxmin' in token:
                    #axis = token[-3].lower()
                    idxType = token[-7:-4]
                    if 'templateYValue' in token:
                        templateAxis = 'x'
                        index = mapParallelIndex(xValueArr, idxType)
                        try:
                            replacedToken = yValueArr[index]
                        except:
                            print(f'{idxType} error at {index} in {title}')
                            replacedToken = yValueArr[len(yValueArr) - 1]
                    elif 'templateXValue' in token:
                        templateAxis = 'y'
                        index = mapParallelIndex(yValueArr, idxType)
                        try:
                            replacedToken = xValueArr[index]
                        except:
                            print(f'{idxType} error at {index} in {title}')
                            replacedToken = xValueArr[len(xValueArr) - 1]
                elif token == 'templateScale':
                    # print("in templateScale: ", token)
                    replacedToken = getScale(titleArr, cleanXLabel, cleanYLabel)
                elif 'templateDelta' in token:
                    indices = str(re.search(r"\[(.+)\]", token).group(0)).replace('[', '').replace(']', '').split(',')
                    index1 = int(indices[0])
                    index2 = int(indices[1])
                    delta = abs(round(float(yValueArr[index1])-float(yValueArr[index2])))
                    replacedToken = str(delta)
                else:
                    index = str(re.search(r"\[(\w+)\]", token).group(0)).replace('[', '').replace(']', '')
                    if 'templateXValue' in token:
                        templateAxis = 'x'
                        index = mapIndex(index, xValueArr)
                        if index < len(xValueArr):
                            replacedToken = xValueArr[index]
                        else:
                            print(f'xvalue index error at {index} in {title}')
                            replacedToken = xValueArr[len(xValueArr) - 1]
                    elif 'templateYValue' in token:
                        templateAxis = 'y'
                        index = mapIndex(index, yValueArr)
                        if index < len(yValueArr):
                            replacedToken = yValueArr[index]
                        else:
                            print(f'yvalue index error at {index} in {title}')
                            replacedToken = yValueArr[len(yValueArr) - 1]
                    elif 'templateXLabel' in token:
                        index = mapIndex(index, cleanXLabel)
                        if index < len(cleanXLabel):
                            replacedToken = cleanXLabel[index]
                        else:
                            print(f'xlabel index error at {index} in {title}')
                            replacedToken = cleanXLabel[len(cleanXLabel) - 1]
                    elif 'templateYLabel' in token:
                        index = mapIndex(index, cleanYLabel)
                        if index < len(cleanYLabel):
                            replacedToken = cleanYLabel[index]
                        else:
                            print(f'ylabel index error at {index} in {title}')
                            replacedToken = cleanYLabel[len(cleanYLabel) - 1]
                    elif 'templateTitleSubject' in token:
                        # print(entities['Subject'][int(index)], index)
                        if int(index) < len(entities['Subject']):
                            replacedToken = entities['Subject'][int(index)]
                        else:
                            print(f'subject index error at {index} in {title}')
                            replacedToken = entities['Subject'][len(entities['Subject']) - 1]
                    elif 'templateTitleDate' in token:
                        # print(entities['Date'][int(index)], index)
                        index = mapIndex(index, entities['Date'])
                        if index < len(entities['Date']):
                            replacedToken = entities['Date'][int(index)]
                        else:
                            print(f'date index error at {index} in {title}')
                            if len(entities['Date']) > 0:
                                replacedToken = entities['Date'][len(entities['Date']) - 1]
                            else:
                                replacedToken = ''
                    elif 'templateTitle' in token:
                        index = mapIndex(index, titleArr)
                        if index < len(titleArr):
                            replacedToken = titleArr[index]
                        else:
                            print(f'title index error at {index} in {title}')
                            replacedToken = titleArr[len(titleArr) - 1]
                # print("Mine: ", token, replacedToken)
                sentenceTemplates[i] = {token:(replacedToken, index, templateAxis)}
            else:
                replacedToken = token
            if i > 2:
                if replacedToken.lower() != reversedTokens[-2].lower() and \
                        replacedToken.lower() != reversedTokens[-1].lower():
                    reversedTokens.append(replacedToken)
                else:
                    print(f'dupe: {replacedToken}')
            else:
                reversedTokens.append(replacedToken)

        reversedTokens = [item for item in reversedTokens if item != '']
        reverse = ' '.join(reversedTokens)
        reverse = replaceTrends(reverse)
        # reverse = reverse.replace(' ,', ',').replace(' .', '.').replace(" '", "'")
        reversedSentences.append(reverse)
        templateList.append(sentenceTemplates)
    # remove empty items
    reverse = ' '.join(reversedSentences)
    finalSentences.append(reverse)


with open('./dataset_barchart/PostProcessedStringComparisonSummaryAfterFixes.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s\n" % line for line in finalSentences)
print(len(finalSentences))

