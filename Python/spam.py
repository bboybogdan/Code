import keyboard

keyboard.wait('space')

for i in range(100):
    keyboard.write('SPAM')
    keyboard.press_and_release('enter')