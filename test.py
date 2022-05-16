import cv2

# 開啟影片檔案
cap = cv2.VideoCapture(0)

# 以迴圈從影片檔案讀取影格，並顯示出來
while (True):
    ret, frame = cap.read()

    # cv2.imshow('frame', frame)
    cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()