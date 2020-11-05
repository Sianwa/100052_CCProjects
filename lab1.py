#The purpose of a lexer is to scan the source code and vreak up each word
#into a list item. Once done it takes these words and creates a type and value pair.

import re

tokens = []
code = 'int result = 100'.split()

RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"
RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numerals = ".[0-9]"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = "([a-zA-Z]+\.[h])"

for word in code:
    if word in RE_Keywords:
        tokens.append(['KEYWORD', word])

    elif re.match(RE_Identifiers, word):
        tokens.append(['IDENTIFIER',word])

    elif word in RE_Operators:
        tokens.append(['OPERATOR', word])

    elif re.match(RE_Special_Characters, word):
        tokens.append(['SPECIAL CHARACTER', word])

    elif re.match(RE_Numerals, word):
            tokens.append(["INTEGER", word[:-1]])

    else:
        print("Unkown token key")
    
       
print(tokens)  