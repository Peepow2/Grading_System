import cv2
from Function import *
# -------------------------------------- #
def Read_AnswerSheet(FILENAME):
    img = cv2.imread(FILENAME)
    
    # Pre processesing
    ratio = 538 / img.shape[1]
    h, w = int(img.shape[0] * ratio), int(img.shape[1] * ratio)
    img = cv2.resize(img, (w, h), interpolation = cv2.INTER_AREA)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, imgThres = cv2.threshold(imgGray, 238, 255, cv2.THRESH_BINARY_INV)

    # Contours
    contours, hierarchy = cv2.findContours(imgThres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    A1, A2 = 55, 90 # 63, 83
    L1, L2 = 35, 50 # 39, 42
    Rect_edge = [[(0, 0), (30, 735)], [(0, 705), (540, 735)]]
    XY = [cv2.boundingRect(cnts) for cnts in contours if IsDetector(A1, A2, L1, L2, Rect_edge, cnts, img)]
    X_axis_detector, Y_axis_detector = sort_contours(XY)

    # ----------------------- Checking ----------------------- #
    W = 10
    Black_Ratio = 0.70

    ID          = Detector(X_axis_detector, Y_axis_detector, (2, 12), (29, 38), W, Black_Ratio, img, imgThres, "Read_ID")
    Subject_ID  = Detector(X_axis_detector, Y_axis_detector, (2, 12), (27, 29), W, Black_Ratio, img, imgThres, "Read_Subject_ID")
    Exam_No     = Detector(X_axis_detector, Y_axis_detector, (26, 27), (3, 8), W, Black_Ratio, img, imgThres, "Read_Exam_No")
    Answer      = Detector(X_axis_detector, Y_axis_detector, (32, 50), (3, 36), W, Black_Ratio, img, imgThres, "Read_Answer")
    Cancel      = Detector(X_axis_detector, Y_axis_detector, (10, 11), (3, 4), W, Black_Ratio, img, imgThres, "Read_Cancel_Point")

    return [(ID, Subject_ID, Exam_No, Cancel), Answer]