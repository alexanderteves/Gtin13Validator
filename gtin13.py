# *_ coding: utf-8 _*_

def isGtin13(gtin13):
    """Checks if argument is a valid GTIN-13 number and returns True or False.""" 
    if len(gtin13) != 13: return False
    
    multiplier = 1
    _sum = 0
    for i in ean[:-1]:
        _sum += int(i) * multiplier
        if multiplier == 1: multiplier = 3
        else: multiplier = 1

    if(_sum % 10) == 0 and ean[12] == 0: return True
    elif(_sum + int(ean[12])) % 10 == 0: return True
    else: return False
