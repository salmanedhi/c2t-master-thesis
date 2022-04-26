## this file checks the coverage of the summary output from the model. It checks how many words from the graph are contained in the summary. 

# this is the output from new model
with open('./NewIzaData vs OldIzaData/NewTemplateOutput.txt', 'r', encoding='utf-8') as file:
    newMatchSummariesArr = file.read().splitlines()

# this is the output from old model
with open('./NewIzaData vs OldIzaData/OldTemplateOutput.txt', 'r', encoding='utf-8') as file:
    oldMatchSummariesArr = file.read().splitlines()

# assert len(newMatchSummariesArr) == len(oldMatchSummariesArr)
# print(len(newMatchSummariesArr))


newLabelCountsArr = []
oldLabelCountsArr = []

newWordCountsArr = []
oldWordCountsArr = []

newLabelArr = []
oldLabelArr = []

for i in range(len(newMatchSummariesArr)):
    newSummary = newMatchSummariesArr[i]
    
    newLabelCount = 0
    newWordCount = 0
    newLabels = ''
    
    newSummaryWords = newSummary.split()
    
    for word in newSummaryWords:
        if 'template' in word:
            newLabels = newLabels + '1 '
            newLabelCount = newLabelCount + 1
        else:
            newLabels = newLabels + '0 '
            newWordCount = newWordCount + 1
     
    newLabelCountsArr.append(newLabelCount)
    newWordCountsArr.append(newWordCount)
    newLabelArr.append(newLabels)

for i in range(len(oldMatchSummariesArr)):
    oldSummary = oldMatchSummariesArr[i]
    
    oldLabelCount = 0
    oldWordCount = 0

    oldLabels = ''

    oldSummaryWords = oldSummary.split()
 
    for word in oldSummaryWords:
        if 'template' in word:
            oldLabels = oldLabels + '1 '
            oldLabelCount = oldLabelCount + 1
        else:
            oldLabels = oldLabels + '0 '
            oldWordCount = oldWordCount + 1
    
    oldLabelCountsArr.append(oldLabelCount)
    oldWordCountsArr.append(oldWordCount)
    oldLabelArr.append(oldLabels)



# this coverage formula is not good since the length of summary can be different for each model and thus is not a good metric for calculating the coverage. 
# print('NEW: ')
# print(sum(newLabelCountsArr))
# print(sum(newLabelCountsArr) / (sum(newLabelCountsArr) + sum(newWordCountsArr)) * 100)

# print('OLD:  ')
# print(sum(oldLabelCountsArr))
# print(sum(oldLabelCountsArr) / (sum(oldLabelCountsArr) + sum(oldWordCountsArr)) * 100)

# assert len(newLabelCountsArr) == len(oldLabelCountsArr)
# assert len(newLabelArr) == len(oldLabelArr)

with open('./NewIzaData vs OldIzaData/NewSummaryLabelCount.txt', mode='wt', encoding='utf8') as myfile1:
    myfile1.writelines("%s\n" % line for line in newLabelCountsArr)

with open('./NewIzaData vs OldIzaData/OldSummaryLabelCount.txt', mode='wt', encoding='utf8') as myfile1:
    myfile1.writelines("%s\n" % line for line in oldLabelCountsArr)

with open('./NewIzaData vs OldIzaData/NewSummaryWordCount.txt', mode='wt', encoding='utf8') as myfile1:
    myfile1.writelines("%s\n" % line for line in newWordCountsArr)

with open('./NewIzaData vs OldIzaData/OldSummaryWordCount.txt', mode='wt', encoding='utf8') as myfile1:
    myfile1.writelines("%s\n" % line for line in oldWordCountsArr)



