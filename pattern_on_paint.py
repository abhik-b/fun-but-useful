import pyautogui,time
time.sleep(8)
pyautogui.click()
distance=400

while distance>0:
    pyautogui.dragRel(distance,0,duration=0.2)
    distance-=50
    pyautogui.dragRel(0,distance,duration=0.2)
    pyautogui.dragRel(-distance,0,duration=0.2)
    distance=distance-50
    pyautogui.dragRel(0,-distance,duration=0.2)