## this file checks the generated labels from preprocessing with the true labels. The true labels were manually done

with open('./dataset_barchart/TrueLabels.txt', 'r', encoding='utf-8') as file:
    trueLabelsArr = file.read().splitlines()

with open('./dataset_barchart/TrueLabelsIds.txt', 'r', encoding='utf-8') as file:
    trueLabelIdsArr = file.read().splitlines()

with open('./dataset_barchart/PreProcesssedExactMatchingSummaryLabel.txt', 'r', encoding='utf-8') as file:
    summaryLabelsArr = file.read().splitlines()

assert len(trueLabelsArr) == len(trueLabelIdsArr)

chartsWithLabelCountsNotSame = 0
chartsWithSameLabelCount = 0
perfectMatchChartsCount = 0
labelMismatchCount = 0
labelMatchCount = 0

for i in range(len(trueLabelIdsArr)):

    perfectMatch = True
    similarityLabels = summaryLabelsArr[int(trueLabelIdsArr[i])-1]
    similarityLabels = similarityLabels.split()
    
    trueLabels = trueLabelsArr[i].split()

    if len(trueLabels) == len(similarityLabels):
        chartsWithSameLabelCount = chartsWithSameLabelCount + 1
        for j in range(len(trueLabels)):
            if int(trueLabels[j]) == int(similarityLabels[j]):
                labelMatchCount = labelMatchCount + 1
            else:
                labelMismatchCount = labelMismatchCount + 1
                perfectMatch = False
        if perfectMatch:
            perfectMatchChartsCount = perfectMatchChartsCount + 1

    else:
        chartsWithLabelCountsNotSame = chartsWithLabelCountsNotSame + 1

print('Total Charts: ', len(trueLabelIdsArr))
print('Charts with same label count: ', chartsWithSameLabelCount)
print('Charts with different label counts: ', chartsWithLabelCountsNotSame) 
print('Charts with perfect label matches ', perfectMatchChartsCount)
print('Total labels mismatch count ', labelMismatchCount)
print('Total Labels match count ', labelMatchCount)
   

