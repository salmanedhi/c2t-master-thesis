## this file performs analysis and generates charts of ratio b/w words and labels in a chart
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

with open('./dataset_barchart/PreProcesssedStringComparisionSummaryLabelCount.txt', 'r', encoding='utf-8') as file:
    labelCountsArr = file.read().splitlines()

with open('./dataset_barchart/PreProcesssedStringComparisionSummaryWordCount.txt', 'r', encoding='utf-8') as file:
    wordCountsArr = file.read().splitlines()

assert len(labelCountsArr) == len(wordCountsArr)
print(len(labelCountsArr))


diffArr = []
diffArrBins = []
wordCountDict = {}

##saving the difference of words-labels for each chart in diffArr
for i in range(len(labelCountsArr)):
    if int(wordCountsArr[i]) > int(labelCountsArr[i]):
        diffArr.append(int(wordCountsArr[i]) - int(labelCountsArr[i]))
    else:
        diffArr.append(int(labelCountsArr[i]) - int(wordCountsArr[i]))

diffArrBins = [0] * len(diffArr)
outliersCount = 0

##Making a dictionary with key as word count and value as number of charts
for i in range(len(diffArr)):
    diffArrBins[diffArr[i]] = diffArrBins[diffArr[i]] + 1 
    if diffArr[i] > 65:
        outliersCount = outliersCount + 1
    if(diffArr[i] == 0):
        print(i)


print('Outliers count ', outliersCount)

##checking if the count of charts matches the total charts we have
count = 0
for i in range(len(diffArrBins)):
     count = count + diffArrBins[i]

assert count == len(labelCountsArr)

##creating dictionary
for i in range(len(diffArrBins)):
    if diffArrBins[i] != 0:
        wordCountDict[i] = diffArrBins[i]

# print(wordCountDict)

##Calculating Quantiles for outlier detection
df = pd.DataFrame(diffArr)
Q1 = df[0].quantile(0.25)
Q3 = df[0].quantile(0.75)
IQR = Q3 - Q1

print('Q1 ', Q1)
print('Q3 ', Q3)
print('IQR ', IQR)
print('lower boundary: ', Q1 - 1.5 * IQR)
print('upper boundary: ', Q3 + 1.5 * IQR)

# print(df[np.logical_or(df[0] < (Q1 - 1.5 * IQR), df[0] > (Q3 + 1.5 * IQR))])

# counts, bins, bars = plt.hist(diffArr)
# plt.show()

# sns.kdeplot(diffArr)
# sns.boxplot(y=diffArr)


##creating a bar plot
x = []
y = []
for key in wordCountDict:
    x.append(key)
    y.append(wordCountDict[key])

plt.bar(x, y)
plt.xlabel("Word Difference Count")
plt.ylabel("No. of charts")


plt.show()
