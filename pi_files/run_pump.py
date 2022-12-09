from gpiozero import LED

led = LED(18)

led.on()
time.sleep(3)
led.off()
