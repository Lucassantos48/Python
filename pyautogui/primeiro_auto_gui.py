import pyautogui
import time

pyautogui.alert('Tire as mãos do teclado e do mouse, Por favor!')
pyautogui.PAUSE = 0.5

#entrar no google drive, esse código precisa ser rodado na maquina local
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('winleft', 'up')
pyautogui.moveTo(417, 300)
pyautogui.click()
time.sleep(2)
pyautogui.write('https://drive.google.com/drive/home')
pyautogui.press('enter')
pyautogui.hotkey('winleft', 'up')
time.sleep(6)

# #entrar na area de trabalho
pyautogui.hotkey('winleft', 'd')

# clicar no arquivo na area de trabalho
pyautogui.moveTo(37, 123)
pyautogui.mouseDown()
pyautogui.moveTo(852, 517)

pyautogui.hotkey('alt', 'tab')

pyautogui.mouseUp()

time.sleep(5)

