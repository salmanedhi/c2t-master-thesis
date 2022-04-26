import jaro
from nltk.stem import WordNetLemmatizer

import Levenshtein as lev


from strsimpy.levenshtein import Levenshtein
from strsimpy.normalized_levenshtein import NormalizedLevenshtein
from strsimpy.jaro_winkler import JaroWinkler
from strsimpy.metric_lcs import MetricLCS
from strsimpy.ngram import NGram
from strsimpy.qgram import QGram
from strsimpy import SIFT4
from strsimpy.cosine import Cosine
from fuzzywuzzy import fuzz

lemmatizer = WordNetLemmatizer()

levenshtein = Levenshtein()
normalized_levenshtein = NormalizedLevenshtein()
jarowinkler = JaroWinkler()
metric_lcs = MetricLCS()
twogram = NGram(2)
threegram = NGram(3)
qgram = QGram(2)
s = SIFT4()
cosine = Cosine(2)


# print(levenshtein.distance('this', 'latvia'))
# print(levenshtein.distance('owning', 'ownership'))
# print()

# print(normalized_levenshtein.distance('this', 'latvia'))
# print(normalized_levenshtein.distance('owning', 'ownership'))
# print()

# print(jarowinkler.similarity('won', 'wins'))
# print(jarowinkler.similarity('games', 'gaming'))
# print()

# print(metric_lcs.distance('this', 'latvia'))
# print(metric_lcs.distance('owning', 'ownership'))
# print()

# print(twogram.distance('this', 'latvia'))
# print(twogram.distance('owning', 'ownership'))
# print()

# print(threegram.distance('this', 'latvia'))
# print(threegram.distance('owning', 'ownership'))
# print()

# print(qgram.distance('this', 'latvia'))
# print(qgram.distance('owning', 'ownership'))
# print()

# print(s.distance('this', 'latvia'))
# print(s.distance('owning', 'ownership'))
# print()

print(cosine.similarity('niche', 'chien'))
# print(cosine.similarity(lemmatizer.lemmatize('owning'), lemmatizer.lemmatize('ownership')))
# print()


# print(fuzz.partial_ratio(lemmatizer.lemmatize('statistic'), lemmatizer.lemmatize('austria')))
# print(fuzz.partial_ratio(lemmatizer.lemmatize('owning'), lemmatizer.lemmatize('ownership')))
# print()

# print(lev.ratio('amazon', 'amazon.com'))
# print(lev.ratio(lemmatizer.lemmatize('owning'), lemmatizer.lemmatize('ownership')))
# print(lev.ratio(lemmatizer.lemmatize('won'), lemmatizer.lemmatize('wins')))
# print(lev.ratio(lemmatizer.lemmatize('games'), lemmatizer.lemmatize('gaming')))


# print(jarowinkler.similarity('foo', 'bar'))
# print(lev.ratio(lemmatizer.lemmatize('foo'), lemmatizer.lemmatize('bar')))

tokens = ['salman', 'edhi']
print(f'1:{tokens[0]} 2:{tokens[1]}')
print()