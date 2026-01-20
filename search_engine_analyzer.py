"""A search engine backend receives raw user search queries.
You need to build a component that:
Normalizes search strings

Extracts filters embedded in text

Tokenizes queries efficiently

Stores query statistics for analysis

The design must remain simple while being extensible and include test cases validating query parsing accuracy."""

import re
class TextCleaner:
    def clean(self, text:str) ->str:
        return text.lower().strip()
class FilterFinder:
    pattern = re.compile(r'(\w+):(\w+)')
    def find_filters(self, text: str):
        filters = dict(self.pattern.findall(text))
        remaining_text = self.pattern.sub('',text).strip()
        return remaining_text, filters
class wordSplitter:
    def split(self, text:str):
        return [word for word in text.split() if word]
    
from collections import defaultdict
class SearchAnalytics:
    def __init__(self):
        self.total_searches = 0
        self.word_count = defaultdict(int)
        self.filter_usage = defaultdict(int)

    def search(self, words, filters):
        self.total_searches += 1
        for word in words:
            self.word_count[word] += 1
        for key in filters:
            self.filter_usage[key] += 1
        return self.total_searches, dict(self.word_count), dict(self.filter_usage)
        
obj = SearchAnalytics()
lst  =  obj.search(["python", "java"], ["category:books", "date:today"])
print(obj.word_count)
print(obj.filter_usage)
print(lst)