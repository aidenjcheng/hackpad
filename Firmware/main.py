# You import all the IOs of your board
import board

# KMK imports
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.encoder import EncoderHandler

# Main keyboard instance
keyboard = KMKKeyboard()

# Add macro extension
macros = Macros()
keyboard.modules.append(macros)

# Button matrix 
PINS = [board.GP3, board.GP4, board.GP2, board.GP1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# rotary encoder setup 
enc = EncoderHandler()


enc.pins = (
    (board.GP28, board.GP27, KC.VOLD, KC.VOLU),
)

keyboard.extensions.append(enc)

keyboard.keymap = [
    [
        # copy and paste
        KC.MACRO(    
            Press(KC.LCTRL),
            Tap(KC.C), 
            Release(KC.LCTRL),
        ), 
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.V),
            Release(KC.LCTRL),
        ), 
        # command palette for vscode
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.P),
            Release(KC.LCTRL),
        ),
        # open terminal in vscode
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.J),
            Release(KC.LCTRL),
        ),
    ]
]

if __name__ == '__main__':
    keyboard.go()
