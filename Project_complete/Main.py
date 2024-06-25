# from Install_package import *
# Install_Package()
# -------------------------------------- #
import os
import time
import shutil
import OMR

S = time.time()

path = ""
for f_AnswerSheet in os.listdir(path):
    DATA = OMR.Read_AnswerSheet(path + '/' + f_AnswerSheet)
    #print(DATA)
    Score = 0
    if not DATA[0][3]:
        for i in range(70):
            if len(DATA[1][i]) == 1 and DATA[1][i] in Solution[1][i]:
                Score += (4 * int(0 <= i < 60)) + (6 * int(60 <= i < 70))
    print(DATA[0][0], '-->', round(Score / 3, 2))
    
try:    
    shutil.rmtree('__pycache__')
except: 
    pass
# Uninstall_Package(p)
# -------------------------------------- #
total = time.time() - S
print('TIME USED =', int(total // 3600), 'hour', int(total // 60), 'min', int(total % 60) + 1, 'seconds')
