import time
import uinput
#keep alive

device = uinput.Device([
    uinput.KEY_E,
    uinput.KEY_H,
    uinput.KEY_L,
    uinput.KEY_O,
])

while True:
        time.sleep(3)
        #press key
        device.emit_click(uinput.KEY_H)
