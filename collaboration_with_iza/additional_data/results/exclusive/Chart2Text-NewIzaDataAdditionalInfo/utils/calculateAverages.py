import os
from statistics import mean

import pandas as pd

punctuation = [';',':', '-', '(', ')', ',']

captionList = os.listdir('../dataset/captions')

captionList.sort()

dataList = os.listdir('../dataset/data/')

dataList.sort()

captionCount = 0
wordCountList = []
sentenceCountList = []

cellCount = 0

vocab = []
for filePath in captionList:
    with open('../dataset/captions/'+filePath,'r', encoding='utf-8') as captionFile:
        caption = captionFile.read()
        captionSentences = caption.split(' . ')
        sentenceCount = len(captionSentences)
        sentenceCountList.append(sentenceCount)
        captionWords = [word for word in caption.split() if word not in punctuation]
        for token in captionWords:
            if token.lower() not in vocab and token.isalpha():
                vocab.append(token.lower())
        wordCount = len(captionWords)
        wordCountList.append(wordCount)
        captionCount += 1


averageWords = sum(wordCountList)/captionCount
print('Mean Token Count: ', averageWords)

averageSentences = sum(sentenceCountList)/captionCount
print('Mean Sentence Count: ', averageSentences)

print('Vocab Size: ', len(vocab))
print('Total Tokens: ', sum(wordCountList))

for dataPath in dataList:
    df = pd.read_csv('../dataset/data/' + dataPath)
    cellCount += (df.size - len(df.columns))

print('Mean Data Cells: ', cellCount / captionCount)

