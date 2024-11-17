"""
充電器を使って、ラズパイの電子部品を起動する為には、main.pyと必ず名前を付けるルールになっている。
その理由は、MicroPythonのルールに従っているからである。
"""

from machine import Pin  # type: ignore
import time

# LED点灯
led = Pin(16, Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)

    print("LED点灯しました")
