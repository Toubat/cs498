import random
import os
import string
import sys
from collections import defaultdict

stop_words = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
    "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
    "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
    "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
])

delimiters = " \t,;.?!-:@[](){}_*/"

def getIndexes(seed):
    random.seed(seed)

    n = 10000
    number_of_lines = 50000
    ret = []

    for i in range(n):
        ret.append(random.randint(0, 50000-1))

    return ret

def process(userID):
    indexes = getIndexes(userID)
    words = []
    counts = defaultdict(int)

    for line in sys.stdin:
        line = line.lower()

        for delimiter in delimiters:
            line = line.replace(delimiter, ' ')

        words.append(line.split())

    for idx in indexes:
        for word in words[idx]:
            if word not in stop_words:
                counts[word] += 1

    freq = [(word, count) for word, count in counts.items()]

    ret = sorted(freq, key=lambda i: (-i[1], i[0]))[:20]

    for word, _ in ret:
        print(word)

process(sys.argv[1])
