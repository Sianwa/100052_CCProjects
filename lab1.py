#The purpose of a lexer is to scan the source code and vreak up each word
#into a list item. Once done it takes these words and creates a type and value pair.

import re

tokens = []
code = 'int result = 100;'.split()

for word in code:
    if word in ['str', 'int', 'bool']:
        tokens.append(['DATATYPE', word])

    elif re.match("[a-z]", word) or re.match("[A - Z]", word):
        tokens.append(['IDENTIFIER',word])

    elif word in '*-/+%=':
        tokens.append(['OPERATOR', word])

    elif re.match(".[0-9]", word):
        if word[len(word) - 1] == ';':
            tokens.append(["INTEGER", word[:-1]])
            tokens.append(['END_STATEMENT', ';'])
        else:
            tokens.append(["INTEGER", word])
print(tokens)  