import keyboard

x = int(input("Cate mesaje vrei sa trimiti? "))

keyboard.wait('space')

for i in range(x):
    keyboard.write('SPAM')
    keyboard.press_and_release('enter')