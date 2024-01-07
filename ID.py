from random import randint
def get_ID(I):
    I += int(randint(3, 10))
    code = ('000' + str(I))[-4:]
    check = sum([int(e) for e in code]) % 10
    return '683' + code + str(check)
