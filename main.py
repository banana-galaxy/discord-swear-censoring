from pynput import keyboard
import pyautogui
pyautogui.PAUSE = 0
typed = []
censor_list = ["fuck", "shit", "motherfucker", "nigga", "bitch"]

def on_press(key):
	global typed, censor_list
	censor = False
	try:
		print(f"alphanumeric key {key.char} pressed")
		char = key.char
		typed.append(char)
	except AttributeError:
		print(f"special key {str(key).split('.')[1]} pressed")
		if str(key).split('.')[1] == 'space':
			char = 'space'
			typed.append(char)
	
	try:
		if typed[len(typed)-1] == 'space' and len(typed) > 1:
			try:
				while True:
					typed.remove('space')
			except ValueError:
				pass
			word = ''.join(typed)
			for i in censor_list:
				if i == word:
					censor = True
			
			if censor:
				pyautogui.press('backspace')
				for i in word:
					pyautogui.press('backspace')
				pyautogui.write('||', interval=0)
				for i in word:
					pyautogui.press(i)
				pyautogui.write('||', interval=0)
				pyautogui.press('space')

			while len(typed) >= 1:
				typed.pop(0)
			word = ''

			print(f"the word is {word}")
	except IndexError:
		print(typed)

def on_release(key):
	print('{0} released'.format(key))
	if key == keyboard.Key.esc:
		# Stop listener
		return False

# Collect events until released
with keyboard.Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
	on_press=on_press,
	on_release=on_release)
listener.start()
