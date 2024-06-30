# from Install_package import *
# Install_Package()
# ---------------------------------------------------------- #
import os
import time
import shutil
import Scoring
import READ_AS
import READ_IMG 
# ---------------------------------------------------------- #
S = time.time()

W = 9
Black_Ratio = 0.85

# READ_Solution
path = "For_Users/Solution"
SOLUTION = dict()
for f_answersheet in os.listdir(path):
    X_axis_detector, Y_axis_detector, imgThres, img = READ_IMG.get_imgThes_and_XY_Detector(path + "/" + f_answersheet)

    Subject_ID  = READ_AS.READ_information(img, imgThres, X_axis_detector, Y_axis_detector, W, Black_Ratio)[1]
    SHADE_Found = READ_AS.READ_SHADE(img, imgThres, X_axis_detector, Y_axis_detector, W, Black_Ratio)
    ANSWER      = Scoring.ConvertXY(SHADE_Found)

    if Subject_ID not in SOLUTION: SOLUTION[Subject_ID] = ANSWER
    #print(SOLUTION)
# ---------------------------------------------------------- #       
# ---------------------------------------------------------- #

# READ_ANSWER
path = "For_Users/AS_Scanned"
for f_answersheet in os.listdir(path):
    X_axis_detector, Y_axis_detector, imgThres, img = READ_IMG.get_imgThes_and_XY_Detector(path + '/' + f_answersheet)

    ID, Subject_ID, Cancel = READ_AS.READ_information(img, imgThres, X_axis_detector, Y_axis_detector, W, Black_Ratio)
    SHADE_Found            = READ_AS.READ_SHADE(img, imgThres, X_axis_detector, Y_axis_detector, W, Black_Ratio)
    ANSWER                 = Scoring.ConvertXY(SHADE_Found)

    Score = 0
    if Subject_ID in SOLUTION:
        Score = Scoring.Score(ANSWER, SOLUTION[Subject_ID]) * int(not Cancel)
    print((ID, Subject_ID, Cancel, Score))
    #print(ANSWER)
    #print(ID, 'Finished')
# ---------------------------------------------------------- #
# ---------------------------------------------------------- #
try:    
    shutil.rmtree('For_Users/__pycache__')
except: 
    pass
# Uninstall_Package()
# ---------------------------------------------------------- #
total = time.time() - S
print('TIME USED =', total, 'seconds')
print('TIME USED =', int(total // 3600), 'hour', int(total // 60), 'min', int(total % 60) + 1, 'seconds')