#works for almost every game that doesnt use intelligence anti afk or smth

from pynput.keyboard import Controller
from pynput.mouse import Controller as MouseController
import time
import random
import ctypes


def detect_keyboard_layout():
    user32 = ctypes.WinDLL("user32", use_last_error=True)
    klid = user32.GetKeyboardLayout(0) & 0xFFFF
    
    # 0x0813 = Belgisch (AZERTY)
    # 0x0409 = Engels (QWERTY - VS)
    if klid == 0x0813:
        return "azerty"
    else:
        return "qwerty"


keyboard_layout = detect_keyboard_layout()
forward_key = "z" if keyboard_layout == "azerty" else "w"

keyboard = Controller()
mouse = MouseController()

def anti_afk():
    print(f"Actief")
    print(f"{keyboard_layout.upper()}, {forward_key}'")

    try:
        while True:
            print(f"loop")
            Random_Sleep_Time = random.uniform(0.1, 1)
            x, y = mouse.position
            mouse.move(random.randint(-5, 5), random.randint(-5, 5))

            keyboard.press(forward_key)
            time.sleep(Random_Sleep_Time)
            keyboard.release(forward_key)
            
            time.sleep(random.uniform(0.1, 1))

            keyboard.press('s')
            time.sleep(Random_Sleep_Time)  
            keyboard.release('s')
            
            time.sleep(random.randint(10, 30))
    except KeyboardInterrupt:
        print("interrupted loser")

if __name__ == "__main__":
    anti_afk()

