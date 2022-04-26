# this file calculates the content selection of the model. Content Selection is calculated by how much of the template variables that existed in the gold summary are present in the generated summary.
from statistics import mean, stdev
from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance
import Levenshtein as lev
from nltk.stem import WordNetLemmatizer

# mainPath = './NewIzaDataShuffled vs OldIzaDataShuffled/'
mainPath = './NewIzaDataFixed vs OldIzaDataFixed/'
# mainPath = './NewIzaData vs OldIzaData/'

goldPath = mainPath + 'OldTestOriginalSummary.txt'
summaryPath = mainPath + 'OldTestSummary.txt'
generatedPath = mainPath + 'OldGenerated.txt'

fillers = ['in', 'the', 'and', 'or', 'an', 'as', 'can', 'be', 'a', ':', '-',
           'to', 'but', 'is', 'of', 'it', 'on', '.', 'at', '(', ')', ',', ';']


lemmatizer = WordNetLemmatizer()

stringMatchingThreshold = 0.85

count = 1

generatedScores = []
baselineScores = []
untemplatedScores = []


with open(summaryPath, 'r', encoding='utf-8') as summaryFile, \
        open(goldPath, 'r', encoding='utf-8') as goldFile, \
            open(generatedPath, 'r', encoding='utf-8') as generatedFile:
    for summary, gold, generated in zip(summaryFile.readlines(), goldFile.readlines(), generatedFile.readlines()):
        summArr = summary.split()
        goldArr = gold.split()
        generatedArr = generated.split()
        recordList = []
        for sums, gld in zip(summArr, goldArr):
            if 'template' in sums and gld.lower() not in fillers and gld.lower() not in recordList:
                recordList.append(gld.lower())
        list1 = recordList
        recordLength = len(recordList)
        generatedList = []
        for token in generatedArr:
            for word in list1:
                # if lev.ratio(lemmatizer.lemmatize(token.lower()), lemmatizer.lemmatize(word)) >= stringMatchingThreshold:
                if token.lower() == word:
                    list1.remove(word)
                    generatedList.append(word)
                    break
      
        count += 1

        generatedRatio = len(generatedList) / recordLength
        generatedScores.append(generatedRatio)


print(f'generated CS stdev: {round(stdev(generatedScores)*100,2)}%')
print()
print(f'generated CS mean: {round(mean(generatedScores)*100,2)}%')
print()
print(f'generated CS RSD: {round((stdev(generatedScores)*100) / abs(mean(generatedScores)),2)}%')

