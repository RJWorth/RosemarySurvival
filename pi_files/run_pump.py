from gpiozero import LED
import time

led = LED(18)


def run_pump(led, duration=5):
    led.on()
    time.sleep(duration)
    led.off()
    return True
