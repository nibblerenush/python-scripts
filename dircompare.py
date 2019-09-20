#!/bin/python3

import difflib
import re
import sys

from os import listdir
from os.path import isfile, join

def GetSources(directory):
  result = list()
  onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
  for f in onlyfiles:
    if (re.match(r'.*\.h', f)):
      result.append(f)
    if (re.match(r'.*\.c', f)):
      result.append(f)
    if (re.match(r'.*\.cpp', f)):
      result.append(f)
  return result

def main():
  dir1 = sys.argv[1]
  sources1 = GetSources(dir1)
  
  dir2 = sys.argv[2]
  sources2 = GetSources(dir2)
  
  for s1 in sources1:
    for s2 in sources2:
      if (s1 == s2):
        text1 = open(join(dir1, s1)).readlines()
        text2 = open(join(dir2, s2)).readlines()
        print("file: ", s1)
        for line in difflib.unified_diff(text1, text2):
          print(line)
        break

if __name__ == "__main__":
  main()
