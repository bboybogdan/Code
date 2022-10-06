import keyboard

x = int(input("Cate mesaje vrei sa trimiti? "))

keyboard.wait('space')

for i in range(x):
    keyboard.write('Vrei o bere?')
    keyboard.press_and_release('enter')