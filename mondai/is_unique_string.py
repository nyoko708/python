#!/usr/bin/env python
# -*- coding: utf-8 -*-

str = u'あいうえおabcdefg'

def is_unique_string(str):
  u"""指定した文字列に重複文字があるか判定する関数

  Keyword arguments:
  str -- string
  """

  str = str.strip()

  unique_flags = {}
  for i in range(0, len(str)):
    val = str[i]
    if val in unique_flags and unique_flags[val] == True:
      return False
    unique_flags[val] = True

  return True

if __name__ == "__main__":
  print is_unique_string(str)
