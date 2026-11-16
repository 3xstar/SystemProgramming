import ctypes
import time

def show_system_message():
    time.sleep(1)

    # 0 - нет родительского окна
    # текст сообщения
    # формат окна
    # заголовок окна
    # иконка информации
    ctypes.windll.user32.MessageBoxW(0, "Внимание!", "Сообщение", 0x10)


show_system_message()

