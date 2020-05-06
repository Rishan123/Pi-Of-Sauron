from sense_emu import SenseHat
import time

sense = SenseHat()


r = (255, 0, 0)
y = (255,255,0)
o = (255,155,0)
b = (0, 0, 0)
sleep = 0.02

# Look straight
anim1straight = [
    r, r, r, r, r, r, r, r,
    r, r, r, y, r, y, r, r,
    r, y, r, y, y, r, y, r,
    r, r, y, b, b, y, r, r,
    r, y, b, b, b, b, y, y,
    r, y, y, b, b, y, y, r,
    r, r, y, y, y, y, r, r,
    r, r, r, r, r, r, r, r
]

anim2straight = [
    r, r, r, r, y, r, r, r,
    y, r, r, y, r, r, r, y,
    r, y, r, r, y, r, y, r,
    y, r, y, b, b, y, y, r,
    r, y, b, b, b, b, r, r,
    r, r, y, b, b, y, y, r,
    y, y, r, y, y, r, y, y,
    r, r, y, r, r, r, r, r
]

anim3straight = [
    r, r, y, r, y, r, r, r,
    r, y, r, y, r, r, r, r,
    r, y, r, r, y, r, y, r,
    r, r, y, b, b, y, r, y,
    r, y, b, b, b, b, y, r,
    r, r, y, b, b, y, r, r,
    r, y, r, y, y, r, y, r,
    y, r, r, r, r, y, r, r
]

# Look left
anim1left = [
    r, r, r, r, r, r, r, r,
    r, y, r, y, r, y, r, r,
    r, y, y, r, y, r, y, r,
    y, b, b, y, y, y, r, r,
    b, b, b, b, y, r, y, r,
    y, b, b, y, y, y, r, r,
    r, y, y, y, y, r, y, r,
    y, r, y, r, r, r, r, r
]

anim2left = [
    r, r, r, r, y, r, r, r,
    y, r, r, y, r, r, r, r,
    r, y, r, r, y, r, y, r,
    y, b, b, y, y, r, r, r,
    b, b, b, b, y, y, r, r,
    y, b, b, y, y, r, y, r,
    y, y, r, y, y, r, r, r,
    r, r, y, r, r, r, r, r
]

anim3left = [
    r, r, r, r, y, r, r, r,
    y, r, y, y, r, y, r, r,
    r, y, r, r, y, r, y, r,
    y, b, b, y, y, r, y, r,
    b, b, b, b, y, y, r, y,
    y, b, b, y, y, r, y, r,
    y, r, r, y, y, y, r, y,
    r, y, y, r, r, r, r, r
]

# Display these colours on the LED matrix

while True:
    sense.set_pixels(anim1left)
    time.sleep(sleep)
    sense.set_pixels(anim2left)
    time.sleep(sleep)
    sense.set_pixels(anim3left)
    time.sleep(sleep)