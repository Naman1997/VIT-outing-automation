import pyautogui


print('Press Ctrl-C to quit.')
try:
	while True:
		x, y = pyautogui.position()
		positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
		print('\b' * len(positionStr), end='', flush=True)
		print(positionStr)
except KeyboardInterrupt:
	print('\nDone.')