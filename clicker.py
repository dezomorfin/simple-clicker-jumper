import keyboard
import pyautogui
import time

clicker = False
jumper = False
print('F6 - clicker\nF7 - exit(work not any click)\nF8 - jumper')
def start_clicker():
    global clicker
    clicker = not clicker
    if clicker == True:
        print('Start')
    else:
        print('Stop')

def start_jumper():
    global jumper
    jumper = not jumper
    if jumper == True:
        print('Jumper on')
    else:
        print('Jumper off')

keyboard.add_hotkey('f6', start_clicker)
keyboard.add_hotkey('f8', start_jumper)

while True:
	if clicker:
		pyautogui.click()
		for sec in range(1):
			if not clicker:
				break
			time.sleep(0.1)
	else:
		time.sleep(0.5)
    
	if jumper:
		pyautogui.keyDown('space')
		for _ in range(5):
			if not jumper:
				break
			time.sleep(0.1)
	else:
		pyautogui.keyUp('space')
		time.sleep(0.5)

	if keyboard.is_pressed('f7'):
		print("Exiting")
		break
