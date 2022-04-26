## This parser transforms chart data from pipe format in txt to csv format
## e.g
#  Age_Group|Under_25|x|bar_chart Revenue_share|7.3|y|bar_chart Age_Group|25-44|x|bar_chart Revenue_share|33.1|y|bar_chart Age_Group|45-64|x|bar_chart Revenue_share|43.5|y|bar_chart Age_Group|65_and_over|x|bar_chart Revenue_share|16.1|y|bar_chart
# will be converted to csv
# Data used is from Thesis\code\Chat2Text_Original\data\train\trainOriginalSummary,trainTitle,trainData.txt
import csv

def readFile(dataPath):
    with open(dataPath, 'r', encoding='utf-8') as dataFile:
        data = dataFile.read()
    return data


chart_no = 143 - 1

#Main Parsing
basePath = 'D:/Saarland/Semesters/Thesis/code/Chart2Text_Original/data/train/'
summaryFile = basePath + 'trainOriginalSummary.txt'
titleFile = basePath + 'trainTitle.txt'
dataFile = basePath + 'trainData.txt'

summaryData = readFile(summaryFile)
titleData = readFile(titleFile)
chartData = readFile(dataFile)


summaryData = summaryData.split('\n')[chart_no]
titleData = titleData.split('\n')[chart_no]
chartData = chartData.split('\n')[chart_no]

print(titleData)
chartData = chartData.split(' ')

# chartData = "Country|Germany|x|bar_chart Number_of_cats_in_thousands|14500|y|bar_chart Country|France|x|bar_chart Number_of_cats_in_thousands|13500|y|bar_chart Country|United_Kingdom|x|bar_chart Number_of_cats_in_thousands|7500|y|bar_chart Country|Italy|x|bar_chart Number_of_cats_in_thousands|7300|y|bar_chart Country|Poland|x|bar_chart Number_of_cats_in_thousands|6400|y|bar_chart Country|Romania|x|bar_chart Number_of_cats_in_thousands|4300|y|bar_chart Country|Spain|x|bar_chart Number_of_cats_in_thousands|3145|y|bar_chart Country|Netherlands|x|bar_chart Number_of_cats_in_thousands|2640|y|bar_chart Country|Belgium|x|bar_chart Number_of_cats_in_thousands|2050|y|bar_chart Country|Austria|x|bar_chart Number_of_cats_in_thousands|2034|y|bar_chart Country|Hungary|x|bar_chart Number_of_cats_in_thousands|2000|y|bar_chart Country|Portugal|x|bar_chart Number_of_cats_in_thousands|1500|y|bar_chart Country|Sweden|x|bar_chart Number_of_cats_in_thousands|1440|y|bar_chart Country|Czechia|x|bar_chart Number_of_cats_in_thousands|1400|y|bar_chart Country|Finland|x|bar_chart Number_of_cats_in_thousands|900|y|bar_chart Country|Bulgaria|x|bar_chart Number_of_cats_in_thousands|800|y|bar_chart Country|Denmark|x|bar_chart Number_of_cats_in_thousands|675|y|bar_chart Country|Lithuania|x|bar_chart Number_of_cats_in_thousands|600|y|bar_chart Country|Greece|x|bar_chart Number_of_cats_in_thousands|600|y|bar_chart Country|Slovakia|x|bar_chart Number_of_cats_in_thousands|550|y|bar_chart Country|Slovenia|x|bar_chart Number_of_cats_in_thousands|480|y|bar_chart Country|Latvia|x|bar_chart Number_of_cats_in_thousands|400|y|bar_chart Country|Ireland|x|bar_chart Number_of_cats_in_thousands|325|y|bar_chart Country|Estonia|x|bar_chart Number_of_cats_in_thousands|285|y|bar_chart"

xLabel = chartData[0].split('|')[0]
yLabel = chartData[1].split('|')[0]

writePath = 'D:/Saarland/Semesters/Thesis/code/Chart2TextCodeExtraction/dataset/'

f = open(writePath+'data/'+str(chart_no+1)+'.csv', 'w', newline='')
writer = csv.writer(f)

writer.writerow([xLabel, yLabel])
for i in range(0, len(chartData)-1, 2):
    x = chartData[i].split('|')[1]
    y = chartData[i+1].split('|')[1]
    writer.writerow([x, y])

f.close()

f = open(writePath+'titles/'+str(chart_no+1)+'.txt', 'w')
f.write(titleData)
f.close()

f = open(writePath+'captions/'+str(chart_no+1)+'.txt', 'w')
f.write(summaryData)
f.close()

