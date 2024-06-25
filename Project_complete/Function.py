import cv2
import numpy as np
# -------------------------------------- #
def sort_contours(contours):
    XY = sorted(contours)
    idx = 0
    for i in range(1, len(XY)):
        if XY[i][0] - XY[i-1][0] >= 15:
            idx = i
            break
    # print(idx)
    return XY[idx:], sorted(XY[0:idx], key = lambda x: x[1])

def IsDetector(A1, A2, L1, L2, Rect_edge, cnts, img):
    if A1 <= cv2.contourArea(cnts) <= A2 and L1 <= cv2.arcLength(cnts, True) <= L2:
        for p in cnts:
            for e in Rect_edge:
                x, y = p[0]
                LU_edge, RD_edge = e
                if (x > LU_edge[0] and x < RD_edge[0]) and (y > LU_edge[1] and y < RD_edge[1]):
                    return True
    return False
# -------------------------------------------- #

# -------------------------------------------- #
def ID_Area(i, j):
    return 2 <= i <= 11 and 27 <= j <= 37

def Exam_No(i, j):
    return i == 26 and (j == 3 or j == 7)

def Answer_Area(i, j):
    return (32 <= i <= 40 or 44 <= i <= 48) and (3 <= j <= 35)

def Cancel_Area(i, j):
    return i == 10 and j == 3

def InCheckArea(i, j):
    return ID_Area(i, j) or Exam_No(i, j) or Answer_Area(i, j) or Cancel_Area(i, j)
# -------------------------------------------- #

# -------------------------------------------- #
def get_No_Ques(i, j):
    col = (j - 3) // 7
    if 32 <= i <= 40: return (9 * col) + int(i - 32)
    if 44 <= i <= 48: return (5 * col) + int(i + 1)

def get_Choice(i, j):
    return str((j - 2) % 7) if 1 <= (j - 2) % 7 <= 5 else ''
# -------------------------------------------- #

# -------------------------------------------- #
def str_Replace_ID(ID, i, j):
    return ID[:j-30] + str(i-2) + ID[j-29:]

def str_Replace_Subject_ID(Subject_ID, i, j):
    return Subject_ID[:j-27] + str(i-2) + Subject_ID[j-26:]

def Exam_number(Exam_NO, i, j):
    Exam_NO += '1' if j == 3 else '2'
    return Exam_NO
def Read_Answer(Answer, i, j):
    Answer[get_No_Ques(i, j)] += get_Choice(i, j)
    return Answer

def Cancel_Point(Bool):
    return Bool
# -------------------------------------------- #

# -------------------------------------------- #
def Detector(X_axis_detector, Y_axis_detector, idx_I, idx_J, W, Black_Ratio, img, imgThres, TYPE_Processing):

    if   TYPE_Processing == 'Read_ID':              OUT = 'XXXXXXXX'
    elif TYPE_Processing == 'Read_Subject_ID':      OUT = 'XX'
    elif TYPE_Processing == 'Read_Answer':          OUT = ['' for i in range(70)]
    elif TYPE_Processing == 'Read_Exam_No':         OUT = ''
    elif TYPE_Processing == 'Read_Cancel_Point':    OUT = False
    else: return "Error"
    
    for i in range(idx_I[0], idx_I[1]):
        x1, y1, w1, h1 = Y_axis_detector[i]
        y1 += 8
        for j in range(idx_J[0], idx_J[1]):
            if not InCheckArea(i, j): continue
                
            x2, y2, w2, h2 = X_axis_detector[j]
            x2 -= 4

            roi = imgThres[y1-W:y1, x2:x2+W]
            black_pixels = np.sum(roi == 255)

            if black_pixels >= (W * W) * Black_Ratio:
                if TYPE_Processing == 'Read_ID': 
                    OUT = str_Replace_ID(OUT, i, j)

                elif TYPE_Processing == 'Read_Subject_ID':
                    OUT = str_Replace_Subject_ID(OUT, i, j)

                elif TYPE_Processing == "Read_Exam_No":
                    OUT = Exam_number(OUT, i, j)

                elif TYPE_Processing == 'Read_Answer':
                    OUT = Read_Answer(OUT, i, j)

                elif TYPE_Processing == 'Read_Cancel_Point':
                    OUT = Cancel_Point(True)

                # cv2.rectangle(img, (x2, y1), (x2 + W, y1 - W), (255, 0, 0), 1)  
    # cv2.imshow('Detected', img)
    # cv2.waitKey(0)
    return OUT
# -------------------------------------------- #

# -------------------------------------------- #