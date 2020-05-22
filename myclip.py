#! python3
# myclip.py - A multi-clipboard program

import sys
import pyperclip

text = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upshell': """Would you consider making this a monthly donation?"""
}

if len(sys.argv) < 2:
    print("Usage: python3 myclip.py [key-phrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print("The text for " +keyphrase+ "is copied to clipboard" )
else:
    print("There is no text for :" +keyphrase)
