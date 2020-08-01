#!/usr/bin/env python3

import json
from youtube_dl.extractor.youtube import YoutubeIE

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        # return None for values that can be encoded to JSON
        return None

tests = []

for test in YoutubeIE._TESTS:
    if "skip" not in test:
        tests.append(test)

with open('testdata/tests.json', 'w') as outfile:
    json.dump(tests, outfile, cls=MyEncoder, indent=4)
