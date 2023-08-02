from re_test_patterns import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [ 'a.',   # a followed by any one character
                'b.',   # b followed by any one character
                'a.*b', # a followed by anything, ending in b
                'a.*?b', # a followed by anything, ending in b
                ])
				

'''
$ python re_charset_dot.py


          11111
012345678901234
abbaaabbbbaaaaa

Matching "a."
   0 :  1 = "ab"
   3 :  4 = "aa"
   5 :  6 = "ab"
  10 : 11 = "aa"
  12 : 13 = "aa"

Matching "b."
   1 :  2 = "bb"
   6 :  7 = "bb"
   8 :  9 = "bb"

Matching "a.*b"
   0 :  9 = "abbaaabbbb"

Matching "a.*?b"
   0 :  1 = "ab"
   3 :  6 = "aaab"
 '''
 