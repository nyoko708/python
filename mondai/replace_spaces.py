#!/usr/bin/env python
# -*- coding: utf-8 -*-

def replace_spaces(str):
  rs = ""
  for num in range(len(str)):
    if str[num] == " ":
      rs += "%20"
    else:
      rs += str[num]

  return rs

if __name__ == "__main__":
  str = "ab c d e "
  print replace_spaces(str)
