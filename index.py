userStr = input('Digite a string a ser invertida: ')
strLen = len(userStr) - 1
reversedStr = ''

while strLen > -1:
    reversedStr += userStr[strLen]
    strLen = strLen - 1
    
print('string invertida: ' + reversedStr)
