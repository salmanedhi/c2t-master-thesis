## this file checks the generated labels from preprocessing with the true labels. The true labels were manually done

with open('./scores', 'r', encoding='utf-8') as file:
    scores = file.read().splitlines()

scoresTotal = 0
for i in range(len(scores)):
    scoresTotal = scoresTotal + float(scores[i])

print(len(scores))
   

print(scoresTotal / len(scores))