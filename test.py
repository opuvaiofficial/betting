from pyautogui import typewrite, press
from time import sleep
text1 = 'bbet 1+1'
text2 = 'bbet 2+1'
text3 = 'bbet 3+1'
sleep(10)
a = 200
for i in range(a):
    typewrite(text1)
    press('enter')
    sleep(2)

    typewrite(text2)
    press('enter')
    sleep(2)

    typewrite(text3)
    press('enter')
    sleep(2)
