from random import randint
def get_ID(I):
    I = int(I[3:-1]) + int(randint(4, 13))
    code = ('0000' + str(I))[-4:]
    check = sum([int(e) for e in code]) % 10
    return '683' + code + str(check)

def Rint(a, b):
    return int(randint(a, b))
