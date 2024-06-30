import cv2
from pos_det import *
# ------------------------------------------------------------------------------------------------------------------ #
def get_imgThes_and_XY_Detector(FILENAME):
    img = cv2.imread(FILENAME) # os.rename(Old_Name, New_Name)
    
    # Pre processesing
    ratio = 538 / img.shape[1]
    h, w = int(img.shape[0] * ratio), int(img.shape[1] * ratio)
    img = cv2.resize(img, (w, h), interpolation = cv2.INTER_AREA)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, imgThres = cv2.threshold(imgGray, 238, 255, cv2.THRESH_BINARY_INV)

    # Contours
    contours, hierarchy = cv2.findContours(imgThres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    A1, A2 = 55, 90
    L1, L2 = 35, 50
    Rect_edge = [[(0, 0), (30, 770)], [(0, 730), (540,770)]]

    XY = [cv2.boundingRect(cnts) for cnts in contours if IsDetector(A1, A2, L1, L2, Rect_edge, cnts, img)]
    X_axis_detector, Y_axis_detector = sort_contours(XY)

    return X_axis_detector, Y_axis_detector, imgThres, img
# ------------------------------------------------------------------------------------------------------------------ #