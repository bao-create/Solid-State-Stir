import time
import board
import busio
import digitalio
import adafruit_max31855

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D4)
cs1 = digitalio.DigitalInOut(board.D5)
cs2 = digitalio.DigitalInOut(board.D6)
cs3 = digitalio.DigitalInOut(board.D5)
cs4 = digitalio.DigitalInOut(board.D5)
cs1 = digitalio.DigitalInOut(board.D5)
cs5 = digitalio.DigitalInOut(board.D5)
cs6 = digitalio.DigitalInOut(board.D5)
cs7 = digitalio.DigitalInOut(board.D5)
cs8 = digitalio.DigitalInOut(board.D5)
cs9 = digitalio.DigitalInOut(board.D5)
cs10 = digitalio.DigitalInOut(board.D5)
cs11 = digitalio.DigitalInOut(board.D5)


print(type(cs))
while True:
    max31855 = adafruit_max31855.MAX31855(spi, cs)

    tempC = max31855.temperature
    tempC = (40.96 * tempC)/53
    tempF = tempC * 9 / 5 + 32
    print("Temperature 1: {} C {} F ".format(tempC, tempF))
    time.sleep(0.3)
    
    max31855 = adafruit_max31855.MAX31855(spi, cs1)
    tempC = max31855.temperature
    tempC = (40.96 * tempC)/53
    tempF = tempC * 9 / 5 + 32
    print("Temperature 2: {} C {} F ".format(tempC, tempF))
    time.sleep(0.3)