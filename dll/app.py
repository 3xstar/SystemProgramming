import ctypes
import time


user32 = ctypes.windll.user32


# Системные константы
# C++ значения вшиты в заголовочных файлах

# Индекс получения расширенных стилей окна
GWL_EXSTYLE = -20
# Флаг, который превращает окно в "слоистое" (поддерживающее прозрачность)
WS_EX_LAYERED = 0x00080000
# Флаг, указывающий на то, что меняем альфа канал (прозрачность)
LWA_ALPHA = 2
WS_EX_TRANSPARENT = 0x00000020

def make_window_ghost():
    time.sleep(3)

    # Получаем HWND (Handle To Window) - id окна
    # Получаем id окна, которое находиться на переднем плане
    hwnd = user32.GetForegroundWindow()
    if not hwnd:
        print("Window not found")
        return

    print(f"Window: {hwnd}")

    # Узнаем текущие стили, чтобы не сломать его
    current_styles = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

    # Добавляем прозрачность
    # Используем побитовое ИЛИ |, чтобы смешать
    # старые стили с флагом WS_EX_LAYERED
    new_style = current_styles | WS_EX_LAYERED
    user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_style)

    # Устанавливаем прозрачность плавно
    for alpha in range(255, 50, -5):
        user32.SetLayeredWindowAttributes(hwnd, 0, alpha, LWA_ALPHA)
        time.sleep(0.05)

    time.sleep(3)

    # Возвращаем в исходное состояние
    for alpha in range(50, 255, 5):
        user32.SetLayeredWindowAttributes(hwnd, 0, alpha, LWA_ALPHA)
        time.sleep(0.02)

    # Снимаем флаг прозрачности, возвращая первоначальный стиль
    user32.SetWindowLongW(hwnd, GWL_EXSTYLE, current_styles)

make_window_ghost()