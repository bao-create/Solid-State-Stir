import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)

p = GPIO.PWM(22, 10000)

p.start(50);
input("press enter to stop")
p.stop
GPIO.cleanup

