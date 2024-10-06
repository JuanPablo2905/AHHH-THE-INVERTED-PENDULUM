from machine import Pin
import time

DIR = 16
STEP = 17
EN = 18

dir_pin = Pin(DIR, Pin.OUT)
step_pin = Pin(STEP, Pin.OUT)
en_pin = Pin(EN, Pin.OUT)

en_pin.value(0)

steps_per_revolution = 200

def move_steps(steps, delay):
    for _ in range(steps):
        step_pin.value(1)
        time.sleep(delay)
        step_pin.value(0)
        time.sleep(delay)

while True:
    dir_pin.value(1)
    move_steps(steps_per_revolution, 0.001)
    time.sleep(1)
    dir_pin.value(0)
    move_steps(steps_per_revolution, 0.001)
    time.sleep(1)