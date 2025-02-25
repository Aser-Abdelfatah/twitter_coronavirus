#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

keys = []
values = []
for k, v in sorted(items[:10]):
    keys.append(k)
    values.append(v)

plt.bar(keys, values, color = "red")

if args.input_path == "reduced.lang":
    plt.title("Hashtag " + args.key + " by Language")
    plt.xlabel("Language")

if args.input_path == "reduced.country":
    plt.title("Hashtag " + args.key + " by Country")
    plt.xlabel("Country")

plt.ylabel("Count")
plt.savefig(args.input_path + args.key + ".png")
plt.show()
