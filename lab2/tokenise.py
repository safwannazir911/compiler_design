from isKeyword import isKeyword
from isIdentifier import isIdentifier
from isConstant import isConstant


def isDelim(x:str)->bool:
    delimiters = [';', ',','(', ')','{', '}','[', ']','\n', '\t',' ']
    return 1 if x in delimiters else 0

def isOperator(x:str)->bool:
    operators = [
    "+", "-", "*", "/", "%", "++", "--", "=", "+=", "-=", "*=", "/=", "%=", 
    "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "&", "|", "^", "~", 
    "<<", ">>", "&=", "|=", "^=", "<<=", ">>=", ".", "->",
    "?", ":", "::"
    ]

    return 1 if x in operators else 0

def isRealNum(s:str)->bool:
    if not s:
        return False
    if s[0] in "+-":
        s = s[1:]

    foundDec = False
    for i in range(len(s)):
        if foundDec == True & s[i]=='.':
            return False
        
        if s[i] == '.':
            foundDec = True

        if not s[i].isnumeric():
            return False
    return True


def processSubstr(string):
    if isKeyword(string): 
        return [string, 'keyword']
    elif isIdentifier(string):
        return [string, 'id']
    elif isConstant(string):
        return [string, 'constant']
    elif isRealNum(string):
        return [string, 'real']
    elif isOperator(string):
        return [string, 'op']
    else: 
        raise ValueError(f"Invalid token: {string}")

   

def parse(text: str):
    tokens = []
    token = ""
    for char in text:
        if isDelim(char):
            if token:
                tokens.append(processSubstr(token))
                token = ""
            if char not in [' ', '\n', '\t']:
                tokens.append([char, 'delim'])
        elif isOperator(char):
            if token:
                tokens.append(processSubstr(token))
                token = ""
            tokens.append([char, 'op'])
        else:
            token += char
    
    # Process the final token if any
    if token:
        tokens.append(processSubstr(token))
    
    return tokens



if __name__ == '__main__':
    text = "int x, y;"
    tok = parse(text)
    print(tok)