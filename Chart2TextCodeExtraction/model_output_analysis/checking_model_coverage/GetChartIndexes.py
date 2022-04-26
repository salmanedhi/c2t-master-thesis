## this file returns the indexes/counts of charts which have better ratio (template_count / word_count) either in the oldmodel or newmodel
import pandas as pd
import numpy as np

with open('./NewIzaData vs OldIzaData/NewIzaSummaryTemplateRatios.txt', 'r', encoding='utf-8') as file:
    newRatiosArr = file.read().splitlines()

with open('./NewIzaData vs OldIzaData/OldIzaSummaryTemplateRatios.txt', 'r', encoding='utf-8') as file:
    oldRatiosArr = file.read().splitlines()

with open('./NewIzaData vs OldIzaData/NewIzaTestTitle.txt', 'r', encoding='utf-8') as file:
    newTestTitlesArr = file.read().splitlines()

with open('./NewIzaData vs OldIzaData/OldIzaTestTitle.txt', 'r', encoding='utf-8') as file:
    oldTestTitlesArr = file.read().splitlines()

assert(len(newRatiosArr) == len(newTestTitlesArr))
assert(len(oldRatiosArr) == len(oldTestTitlesArr))

chartNosWithOldRatioGreaterArr = []
chartNosWithNewRatioGreaterArr = []
chartsWithSameRatio = 0

##saving the difference of words-labels for each chart in diffArr
for i in range(len(oldRatiosArr)):
    if(oldTestTitlesArr[i] in newTestTitlesArr):
        title = oldTestTitlesArr[i]
        newIndex = newTestTitlesArr.index(title)

        if(oldRatiosArr[i] > newRatiosArr[newIndex]):
            chartNosWithOldRatioGreaterArr.append(i)
        elif(newRatiosArr[newIndex] > oldRatiosArr[i]):
            chartNosWithNewRatioGreaterArr.append(newIndex)
        else:
            chartsWithSameRatio = chartsWithSameRatio + 1


print(len(chartNosWithOldRatioGreaterArr))
print(len(chartNosWithNewRatioGreaterArr))
print(chartsWithSameRatio)
print(chartNosWithOldRatioGreaterArr)
print(oldTestTitlesArr[chartNosWithOldRatioGreaterArr[1]])
# with open('./NewBarSummaryTemplateRatios.txt', mode='wt', encoding='utf8') as myfile1:
    # myfile1.writelines("%s\n" % line for line in ratioArr)