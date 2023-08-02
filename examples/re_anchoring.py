from re_test_patterns import test_patterns

test_patterns('This is some text -- with punctuation.',
              [ r'^\w+',     # word at start of string
                r'\A\w+',    # word at start of string
                r'\w+\S*$',  # word at end of string, with optional punctuation
                r'\w+\S*\Z', # word at end of string, with optional punctuation
                r'\w*t\w*',  # word containing 't'
                r'\bt\w+',   # 't' at start of word
                r'\w+t\b',   # 't' at end of word
                r'\Bt\B',    # 't', not start or end of word
                ])

'''
$ python re_anchoring.py


          1111111111222222222233333333
01234567890123456789012345678901234567
This is some text -- with punctuation.

Matching "^\w+"
   0 :  3 = "This"

Matching "\A\w+"
   0 :  3 = "This"

Matching "\w+\S*$"
  26 : 37 = "punctuation."

Matching "\w+\S*\Z"
  26 : 37 = "punctuation."

Matching "\w*t\w*"
  13 : 16 = "text"
  21 : 24 = "with"
  26 : 36 = "punctuation"

Matching "\bt\w+"
  13 : 16 = "text"

Matching "\w+t\b"
  13 : 16 = "text"

Matching "\Bt\B"
  23 : 23 = "t"
  30 : 30 = "t"
  33 : 33 = "t
  "
  '''