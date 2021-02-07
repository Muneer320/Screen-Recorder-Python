import numpy as np
import cv2
import pyautogui
import tempfile

fileName = tempfile.mktemp(prefix="output_", suffix=".mp4", dir="")
print(fileName)

screenSize = (1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(fileName, fourcc, 20.0, (screenSize))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("show", frame)
    if cv2.waitKey(1)==ord("q"):
        break
