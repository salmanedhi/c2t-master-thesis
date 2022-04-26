## this file gets the template label counts of each chart and saves it in a file

with open('./dataset_barchart/PreProcesssedExactMatchingSummary.txt', 'r', encoding='utf-8') as file:
    exactMatchSummariesArr = file.read().splitlines()

with open('./dataset_barchart/PreProcesssedStringComparisionSummary.txt', 'r', encoding='utf-8') as file:
    similarityMatchSummariesArr = file.read().splitlines()

assert len(exactMatchSummariesArr) == len(similarityMatchSummariesArr)
print(len(exactMatchSummariesArr))


exactLabelCountsArr = []
similarityLabelCountsArr = []

exactWordCountsArr = []
similarityWordCountsArr = []

exctLabelArr = []
similarityLabelArr = []

for i in range(len(exactMatchSummariesArr)):
    exactSummary = exactMatchSummariesArr[i]
    similaritySummary = similarityMatchSummariesArr[i]
    
    exactLabelCount = 0
    exactWordCount = 0
    similarityLabelCount = 0
    similarityWordCount = 0

    exactLabels = ''
    similarityLabels = ''

    exactSummaryWords = exactSummary.split()
    similaritySummaryWords = similaritySummary.split()

    for word in exactSummaryWords:
        if 'template' in word:
            exactLabels = exactLabels + '1 '
            exactLabelCount = exactLabelCount + 1
        else:
            exactLabels = exactLabels + '0 '
            exactWordCount = exactWordCount + 1
     
    for word in similaritySummaryWords:
        if 'template' in word:
            similarityLabels = similarityLabels + '1 '
            similarityLabelCount = similarityLabelCount + 1
        else:
            similarityLabels = similarityLabels + '0 '
            similarityWordCount = similarityWordCount + 1
    
    exactLabelCountsArr.append(exactLabelCount)
    similarityLabelCountsArr.append(similarityLabelCount)

    exactWordCountsArr.append(exactWordCount)
    similarityWordCountsArr.append(similarityWordCount)

    exctLabelArr.append(exactLabels)
    similarityLabelArr.append(similarityLabels)

assert len(exactLabelCountsArr) == len(similarityLabelCountsArr)
assert len(exctLabelArr) == len(similarityLabelArr)

print(sum(exactLabelCountsArr) / (sum(exactLabelCountsArr) + sum(exactWordCountsArr)) * 100)
print(sum(similarityLabelCountsArr) / (sum(similarityLabelCountsArr) + sum(similarityWordCountsArr)) * 100)

# with open('./dataset_barchart/PreProcesssedExactMatchingSummaryLabelCount.txt', mode='wt', encoding='utf8') as myfile1:
#     myfile1.writelines("%s\n" % line for line in exactLabelCountsArr)

# with open('./dataset_barchart/PreProcesssedStringComparisionSummaryLabelCount.txt', mode='wt', encoding='utf8') as myfile1:
#     myfile1.writelines("%s\n" % line for line in similarityLabelCountsArr)

# with open('./dataset_barchart/PreProcesssedExactMatchingSummaryWordCount.txt', mode='wt', encoding='utf8') as myfile1:
#     myfile1.writelines("%s\n" % line for line in exactWordCountsArr)

# with open('./dataset_barchart/PreProcesssedStringComparisionSummaryWordCount.txt', mode='wt', encoding='utf8') as myfile1:
#     myfile1.writelines("%s\n" % line for line in similarityWordCountsArr)

# with open('./dataset_barchart/PreProcesssedExactMatchingSummaryLabel.txt', mode='wt', encoding='utf8') as myfile1:
#     myfile1.writelines("%s\n" % line for line in exctLabelArr)

# with open('./dataset_barchart/PreProcesssedStringComparisionSummaryLabel.txt', mode='wt', encoding='utf8') as myfile1:
#     myfile1.writelines("%s\n" % line for line in similarityLabelArr)


