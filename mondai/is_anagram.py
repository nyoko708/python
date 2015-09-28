#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_anagram(str1, str2):

  strs1 = _sort(str1)
  strs2 = _sort(str2)

  if strs1 != strs2:
    return False

  return True

def _sort(str):
  str = str.strip().replace(' ', '')
  strs = list(str)
  strs.sort()
  return strs

if __name__ == "__main__":
  str1 = "anagrams"
  str2 = "ars magna"
  print is_anagram(str1, str2)
