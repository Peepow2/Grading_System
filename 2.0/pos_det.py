import cv2
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