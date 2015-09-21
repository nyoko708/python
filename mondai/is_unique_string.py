#!/usr/bin/env python
# -*- coding: utf-8 -*-

str = u'あいうえおabcdefg'

def is_unique_string(str):
  u"""指定した文字列に重複文字があるか判定する関数

  Keyword arguments:
  str -- string
  """

  strs = []
  for i in range(0, len(str)):
    strs.append(str[i])

  is_unique_flags = {}
  for i in range(0, len(str)):
    val = strs[i]
    if val in is_unique_flags and is_unique_flags[val] == True:
      return False
    is_unique_flags[val] = True

  return True

if __name__ == "__main__":
  print is_unique_string(str)
