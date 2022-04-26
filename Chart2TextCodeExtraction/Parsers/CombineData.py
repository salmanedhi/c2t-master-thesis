# this file combines the data of bar and iza. 
#location: Thesis\code\Final Training Data Sets\bar_chart_data_new and Thesis\code\Final Training Data Sets\iza_data_new

def openData(path):
    with open(path, 'r', encoding='utf-8') as captionFile:
        data = captionFile.readlines()
    return data

bar_data_path = '../../Final Training Data Sets/bar_chart_data_old'
iza_data_path = '../../Final Training Data Sets/iza_data_old'
write_path = '../../Final Training Data Sets/bar_iza_data_old'

 

# titleList file
bar_titles = openData(bar_data_path + '/titleList.txt')
iza_titles = openData(iza_data_path + '/titleList.txt')

print(len(bar_titles))
print(len(iza_titles))
titles = bar_titles + iza_titles

with open(write_path + '/titleList.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in titles)


# summaryList file
bar_summaries = openData(bar_data_path + '/summaryList.txt')
iza_summaries = openData(iza_data_path + '/summaryList.txt')

print(len(bar_summaries))
print(len(iza_summaries))
summaries = bar_summaries + iza_summaries

with open(write_path + '/summaryList.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in summaries)


# test folder
testDataBar = openData(bar_data_path + '/test/testData.txt')
testDataLabelBar = openData(bar_data_path + '/test/testDataLabel.txt')
testOriginalSummaryBar = openData(bar_data_path + '/test/testOriginalSummary.txt')
testSummaryBar = openData(bar_data_path + '/test/testSummary.txt')
testSummaryLabelBar = openData(bar_data_path + '/test/testSummaryLabel.txt')
testTitleBar = openData(bar_data_path + '/test/testTitle.txt')

testDataIza = openData(iza_data_path + '/test/testData.txt')
testDataLabelIza = openData(iza_data_path + '/test/testDataLabel.txt')
testOriginalSummaryIza = openData(iza_data_path + '/test/testOriginalSummary.txt')
testSummaryIza = openData(iza_data_path + '/test/testSummary.txt')
testSummaryLabelIza = openData(iza_data_path + '/test/testSummaryLabel.txt')
testTitleIza = openData(iza_data_path + '/test/testTitle.txt')

testData = testDataBar + testDataIza
testDataLabel = testDataLabelBar + testDataLabelIza
testOriginalSummary = testOriginalSummaryBar + testOriginalSummaryIza
testSummary = testSummaryBar + testSummaryIza
testSummaryLabel = testSummaryLabelBar + testSummaryLabelIza
testTitle = testTitleBar + testTitleIza


with open(write_path + '/test/testData.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in testData)

with open(write_path + '/test/testDataLabel.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in testDataLabel)

with open(write_path + '/test/testOriginalSummary.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in testOriginalSummary)

with open(write_path + '/test/testSummary.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in testSummary)

with open(write_path + '/test/testSummaryLabel.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in testSummaryLabel)

with open(write_path + '/test/testTitle.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in testTitle)


# train folder
trainDataBar = openData(bar_data_path + '/train/trainData.txt')
trainDataLabelBar = openData(bar_data_path + '/train/trainDataLabel.txt')
trainOriginalSummaryBar = openData(bar_data_path + '/train/trainOriginalSummary.txt')
trainSummaryBar = openData(bar_data_path + '/train/trainSummary.txt')
trainSummaryLabelBar = openData(bar_data_path + '/train/trainSummaryLabel.txt')
trainTitleBar = openData(bar_data_path + '/train/trainTitle.txt')

trainDataIza = openData(iza_data_path + '/train/trainData.txt')
trainDataLabelIza = openData(iza_data_path + '/train/trainDataLabel.txt')
trainOriginalSummaryIza = openData(iza_data_path + '/train/trainOriginalSummary.txt')
trainSummaryIza = openData(iza_data_path + '/train/trainSummary.txt')
trainSummaryLabelIza = openData(iza_data_path + '/train/trainSummaryLabel.txt')
trainTitleIza = openData(iza_data_path + '/train/trainTitle.txt')

trainData = trainDataBar + trainDataIza
trainDataLabel = trainDataLabelBar + trainDataLabelIza
trainOriginalSummary = trainOriginalSummaryBar + trainOriginalSummaryIza
trainSummary = trainSummaryBar + trainSummaryIza
trainSummaryLabel = trainSummaryLabelBar + trainSummaryLabelIza
trainTitle = trainTitleBar + trainTitleIza


with open(write_path + '/train/trainData.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in trainData)

with open(write_path + '/train/trainDataLabel.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in trainDataLabel)

with open(write_path + '/train/trainOriginalSummary.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in trainOriginalSummary)

with open(write_path + '/train/trainSummary.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in trainSummary)

with open(write_path + '/train/trainSummaryLabel.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in trainSummaryLabel)

with open(write_path + '/train/trainTitle.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in trainTitle)



# Valid Folder
validDataBar = openData(bar_data_path + '/valid/validData.txt')
validDataLabelBar = openData(bar_data_path + '/valid/validDataLabel.txt')
validOriginalSummaryBar = openData(bar_data_path + '/valid/validOriginalSummary.txt')
validSummaryBar = openData(bar_data_path + '/valid/validSummary.txt')
validSummaryLabelBar = openData(bar_data_path + '/valid/validSummaryLabel.txt')
validTitleBar = openData(bar_data_path + '/valid/validTitle.txt')

validDataIza = openData(iza_data_path + '/valid/validData.txt')
validDataLabelIza = openData(iza_data_path + '/valid/validDataLabel.txt')
validOriginalSummaryIza = openData(iza_data_path + '/valid/validOriginalSummary.txt')
validSummaryIza = openData(iza_data_path + '/valid/validSummary.txt')
validSummaryLabelIza = openData(iza_data_path + '/valid/validSummaryLabel.txt')
validTitleIza = openData(iza_data_path + '/valid/validTitle.txt')

validData = validDataBar + validDataIza
validDataLabel = validDataLabelBar + validDataLabelIza
validOriginalSummary = validOriginalSummaryBar + validOriginalSummaryIza
validSummary = validSummaryBar + validSummaryIza
validSummaryLabel = validSummaryLabelBar + validSummaryLabelIza
validTitle = validTitleBar + validTitleIza


with open(write_path + '/valid/validData.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in validData)

with open(write_path + '/valid/validDataLabel.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in validDataLabel)

with open(write_path + '/valid/validOriginalSummary.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in validOriginalSummary)

with open(write_path + '/valid/validSummary.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in validSummary)

with open(write_path + '/valid/validSummaryLabel.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in validSummaryLabel)

with open(write_path + '/valid/validTitle.txt', mode='wt', encoding='utf8') as myfile0:
    myfile0.writelines("%s" % line for line in validTitle)