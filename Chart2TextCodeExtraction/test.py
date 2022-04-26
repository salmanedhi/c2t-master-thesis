from bleurt import score

checkpoint = "BLEURT-20"
references = ["This is a test."]
candidates = ["This is the test."]

scorer = score.BleurtScorer()
scores = scorer.score(references=references, candidates=candidates)
assert type(scores) == list and len(scores) == 1
print(scores)