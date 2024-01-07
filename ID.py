from random import randint

def reset_pass():
    p = open('pass_init.txt', 'w')
    p.write('0')
    p.close()
    return 

def saved_pass():
    p = open('pass_init.txt', 'r')
    I = int(p.readline()) + int(randint(3, 10))
    p.close()
    p = open('pass_init.txt', 'w')
    p.write(str(I))
    p.close()
    return I

def get_ID():    
    I = saved_pass()
    code = ('0000' + str(I))[-4:]
    check = ((int(code[0]) * 3 + int(code[1]) * 5 + \
            int(code[2]) * 7 + int(code[3]) * 11) * 13) % 10
    return '683' + code + str(check)