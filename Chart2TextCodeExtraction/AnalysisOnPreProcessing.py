## this file performs analysis on the preprocessing template assigning of chart summaries b/w exact matching and string comparision.


##Below code opens the label counts file of each chart and then counts the average labels per chart in both exact matching and string similarity approach.

exactMatchLabelCountArr = []
similarityMatchLabelCountArr = []

with open('./dataset_barchart/15-july-2021/CustomExactMatchingSummaryLabelCount.txt', 'r', encoding='utf-8') as file:
    exactMatchLabelCountArr = file.read().splitlines()

with open('./dataset_barchart/15-july-2021/CustomStringComparisionSummaryLabelCount.txt', 'r', encoding='utf-8') as file:
    similarityMatchLabelCountArr = file.read().splitlines()

assert len(exactMatchLabelCountArr) == len(similarityMatchLabelCountArr)


exactCountGreater = 0
similarityCountGreater = 0
totalExactLabelsCount = 0
totalSimilarityLabelsCount = 0
sameCount = 0

for i in range(len(exactMatchLabelCountArr)):
    totalExactLabelsCount = totalExactLabelsCount + int(exactMatchLabelCountArr[i])
    totalSimilarityLabelsCount = totalSimilarityLabelsCount + int(similarityMatchLabelCountArr[i]) 

    if int(similarityMatchLabelCountArr[i]) > int(exactMatchLabelCountArr[i]):
        similarityCountGreater = similarityCountGreater + 1
    elif int(exactMatchLabelCountArr[i]) > int(similarityMatchLabelCountArr[i]):
        exactCountGreater = exactCountGreater + 1
        # print (i, exactMatchLabelCountArr[i], similarityMatchLabelCountArr[i])
    else:
        sameCount = sameCount + 1

avgLabelCountPerChartExact = totalExactLabelsCount / len(exactMatchLabelCountArr)
avgLabelCountPerChartSimilarity = totalSimilarityLabelsCount / len(exactMatchLabelCountArr)


print('Total Charts: ',len(exactMatchLabelCountArr))
print('Charts with Exact & Similar Count Same: ', exactCountGreater+sameCount)
print('Charts with Similairy Count Greater: ', similarityCountGreater)
print('Total Exact Labels Count: ', totalExactLabelsCount)
print('Total Similarity Labels Count: ', totalSimilarityLabelsCount)
print('Avg. Label count per chart in Exact Approach: ', avgLabelCountPerChartExact)
print('Avg. Label count per chart in Similarity Approach: ', avgLabelCountPerChartSimilarity)
print('Avg. Increase in Count when using Similarity Approach: ', avgLabelCountPerChartSimilarity - avgLabelCountPerChartExact)



print('#########################')
#Comparing old exact counts with new exact counts. Date issue fixed
with open('./dataset_barchart/CustomExactMatchingSummaryLabelCount.txt', 'r', encoding='utf-8') as file:
    exactMatchLabelCountArrNew = file.read().splitlines()

with open('./dataset_barchart/15-july-2021/CustomExactMatchingSummaryLabelCount.txt', 'r', encoding='utf-8') as file:
    exactMatchLabelCountArrOld = file.read().splitlines()

assert len(exactMatchLabelCountArrOld) == len(exactMatchLabelCountArrNew)

exactOldCountGreater = 0
exactNewCountGreater = 0
totalExactOldLabelsCount = 0
totalExactNewLabelsCount = 0
sameCount = 0

for i in range(len(exactMatchLabelCountArrOld)):
    totalExactOldLabelsCount = totalExactOldLabelsCount + int(exactMatchLabelCountArrOld[i])
    totalExactNewLabelsCount = totalExactNewLabelsCount + int(exactMatchLabelCountArrNew[i]) 

    if int(exactMatchLabelCountArrOld[i]) > int(exactMatchLabelCountArrNew[i]):
        exactOldCountGreater = exactOldCountGreater + 1
        # print(i)
    elif int(exactMatchLabelCountArrNew[i]) > int(exactMatchLabelCountArrOld[i]):
        exactNewCountGreater = exactNewCountGreater + 1
    else:
        sameCount = sameCount + 1

print('Total Charts: ',len(exactMatchLabelCountArr))
print('Charts with Exact Old & Exact New Count Same: ', sameCount)
print('Charts with Exact New Count Greater: ', exactNewCountGreater)
print('Charts with Exact Old Count Greater: ', exactOldCountGreater)
print('Total Exact Old Labels Count: ', totalExactOldLabelsCount)
print('Total Exact New Labels Count: ', totalExactNewLabelsCount)

print('#########################')

#Comparing old similarity counts with new similarity counts. Date issue fixed
with open('./dataset_barchart/CustomStringComparisionSummaryLabelCount.txt', 'r', encoding='utf-8') as file:
    exactMatchLabelCountArrNew = file.read().splitlines()

with open('./dataset_barchart/15-july-2021/CustomStringComparisionSummaryLabelCount.txt', 'r', encoding='utf-8') as file:
    exactMatchLabelCountArrOld = file.read().splitlines()

assert len(exactMatchLabelCountArrOld) == len(exactMatchLabelCountArrNew)

exactOldCountGreater = 0
exactNewCountGreater = 0
totalExactOldLabelsCount = 0
totalExactNewLabelsCount = 0
sameCount = 0

for i in range(len(exactMatchLabelCountArrOld)):
    totalExactOldLabelsCount = totalExactOldLabelsCount + int(exactMatchLabelCountArrOld[i])
    totalExactNewLabelsCount = totalExactNewLabelsCount + int(exactMatchLabelCountArrNew[i]) 

    if int(exactMatchLabelCountArrOld[i]) > int(exactMatchLabelCountArrNew[i]):
        exactOldCountGreater = exactOldCountGreater + 1
    elif int(exactMatchLabelCountArrNew[i]) > int(exactMatchLabelCountArrOld[i]):
        exactNewCountGreater = exactNewCountGreater + 1
    else:
        sameCount = sameCount + 1

print('Total Charts: ',len(exactMatchLabelCountArr))
print('Charts with Old & New Count Same: ', sameCount)
print('Charts with New Count Greater: ', exactNewCountGreater)
print('Charts with Old Count Greater: ', exactOldCountGreater)
print('Total Old Labels Count: ', totalExactOldLabelsCount)
print('Total New Labels Count: ', totalExactNewLabelsCount)


print('#########################')
exactMatchLabelCountArr = []
similarityMatchLabelCountArr = []

with open('./dataset_barchart/15-july-2021/CustomExactMatchingSummaryLabelCount.txt', 'r', encoding='utf-8') as file:
    exactMatchLabelCountArr = file.read().splitlines()

with open('./dataset_barchart/CustomStringComparisionSummaryLabelCount.txt', 'r', encoding='utf-8') as file:
    similarityMatchLabelCountArr = file.read().splitlines()

assert len(exactMatchLabelCountArr) == len(similarityMatchLabelCountArr)


exactCountGreater = 0
similarityCountGreater = 0
totalExactLabelsCount = 0
totalSimilarityLabelsCount = 0
sameCount = 0

for i in range(len(exactMatchLabelCountArr)):
    totalExactLabelsCount = totalExactLabelsCount + int(exactMatchLabelCountArr[i])
    totalSimilarityLabelsCount = totalSimilarityLabelsCount + int(similarityMatchLabelCountArr[i]) 

    if int(similarityMatchLabelCountArr[i]) > int(exactMatchLabelCountArr[i]):
        similarityCountGreater = similarityCountGreater + 1
    elif int(exactMatchLabelCountArr[i]) > int(similarityMatchLabelCountArr[i]):
        exactCountGreater = exactCountGreater + 1
        # print (i, exactMatchLabelCountArr[i], similarityMatchLabelCountArr[i])
    else:
        sameCount = sameCount + 1

avgLabelCountPerChartExact = totalExactLabelsCount / len(exactMatchLabelCountArr)
avgLabelCountPerChartSimilarity = totalSimilarityLabelsCount / len(exactMatchLabelCountArr)


print('Total Charts: ',len(exactMatchLabelCountArr))
print('Charts with Exact & Similar Count Same: ', exactCountGreater+sameCount)
print('Charts with Similairy Count Greater: ', similarityCountGreater)
print('Total Exact Labels Count: ', totalExactLabelsCount)
print('Total Similarity Labels Count: ', totalSimilarityLabelsCount)
print('Avg. Label count per chart in Exact Approach: ', avgLabelCountPerChartExact)
print('Avg. Label count per chart in Similarity Approach: ', avgLabelCountPerChartSimilarity)
print('Avg. Increase in Count when using Similarity Approach: ', avgLabelCountPerChartSimilarity - avgLabelCountPerChartExact)