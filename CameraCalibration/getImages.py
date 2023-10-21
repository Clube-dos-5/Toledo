import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

num = 0

while cap.isOpened():

    succes, img = cap.read()

    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'):  # wait for 's' key to save and exit
        cv2.imwrite('../images/img' + str(num) + '.png', img)
        print(f'Imagem {num} salva!')
        num += 1

    cv2.imshow('Img', img)

# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows()
