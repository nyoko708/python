#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse_string(str):
  u"""指定した文字列を逆さにする関数

  Keyword arguments:
  str -- string
  """

  reverse = ""
  for i in range(len(str)-1, -1, -1):
    reverse = reverse + str[i:i+1]

  return reverse

if __name__ == "__main__":
  str = u"あ　いうえお　ab  cdefg"
  print reverse_string(str)
