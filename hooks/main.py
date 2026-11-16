import keyboard
import time

def on_space_press(event):
    print("Hook worked!")

def main():
    # supress = True, мы "убиваем" сигнал после перехвата
    # не пустили сигнал в систему
    keyboard.on_press_key("space", on_space_press)

    # Программа ждет нажатия esc
    keyboard.wait("esc")


main()