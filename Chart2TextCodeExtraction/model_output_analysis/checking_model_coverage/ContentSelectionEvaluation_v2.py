# this file calculates the content selection part 2 of the model. Content Selection v2 is calculated by how much of the template variables that existed in the generated summary are also in the gold summary.
# this is the opposite of what we did in ContentSelectionEvaluation v1.
from statistics import mean, stdev
from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance
import Levenshtein as lev
from nltk.stem import WordNetLemmatizer


# mainPath = './NewIzaDataShuffled vs OldIzaDataShuffled/'
mainPath = './NewIzaDataFixed vs OldIzaDataFixed/'
# mainPath = './NewIzaData vs OldIzaData/'

goldPath = mainPath + 'NewTestOriginalSummary.txt'
generatedPath = mainPath + 'NewTemplateOutput.txt'
generatedWithoutTemplatePath = mainPath + 'NewGenerated.txt'

fillers = ['in', 'the', 'and', 'or', 'an', 'as', 'can', 'be', 'a', ':', '-',
           'to', 'but', 'is', 'of', 'it', 'on', '.', 'at', '(', ')', ',', ';']


lemmatizer = WordNetLemmatizer()

stringMatchingThreshold = 0.85

count = 1

generatedScores = []
baselineScores = []
untemplatedScores = []


with open(goldPath, 'r', encoding='utf-8') as goldFile, \
            open(generatedPath, 'r', encoding='utf-8') as generatedFile, \
                open(generatedWithoutTemplatePath, 'r', encoding='utf-8') as generatedWithoutTemplateFile:
    for gold, generated, generatedWithoutTemplate in zip(goldFile.readlines(), generatedFile.readlines(), generatedWithoutTemplateFile.readlines()):
        goldArr = gold.split()
        generatedArr = generated.split()
        generatedWithoutTemplatesArr = generatedWithoutTemplate.split()
        recordList = []
        for gen, genWT in zip(generatedArr, generatedWithoutTemplatesArr):
            if 'template' in gen and genWT.lower() not in fillers and genWT.lower() not in recordList:
                recordList.append(genWT.lower())
        list1 = recordList
        recordLength = len(recordList)
        generatedList = []
        for token in goldArr:
            for word in list1:
                if lev.ratio(lemmatizer.lemmatize(token.lower()), lemmatizer.lemmatize(word)) >= stringMatchingThreshold:
                # if token.lower() == word:
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

