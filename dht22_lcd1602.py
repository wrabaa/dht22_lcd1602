from RPLCD.i2c import CharLCD
import Adafruit_DHT
import time
import sys
import RPi.GPIO as GPIO

# Replace 0x27 with the I2C address of your LCD module
lcd = CharLCD('PCF8574', 0x27)

# Set the sensor type and the GPIO pin
sensor = Adafruit_DHT.DHT22
pin = 4  # Replace 4 with the actual GPIO pin number you've connected the DHT22 to

# Set the LED GPIO pin
led_pin = 17  # Replace 17 with the actual GPIO pin number for the LED

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, GPIO.LOW)  # Turn off the LED initially

try:
    while True:
        # Attempt to get sensor reading
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # Display readings on the LCD if they are valid
        if humidity is not None and temperature is not None:
            # Display readings on the LCD
            lcd.cursor_pos = (0, 0)  # Set cursor to the beginning of the first line
            lcd.write_string(f"Temp: {temperature:.2f}C")
            lcd.cursor_pos = (1, 0)  # Set cursor to the beginning of the second line
            lcd.write_string(f"Humi: {humidity:.2f}%")
            GPIO.output(led_pin, GPIO.HIGH)  # Turn on the LED
        else:
            # Clear the LCD and turn off the LED
            lcd.clear()
            lcd.write_string("Failed to retrieve\nsensor data")
            GPIO.output(led_pin, GPIO.LOW)  # Turn off the LED

        time.sleep(2)  # Wait for a few seconds before taking another reading

except KeyboardInterrupt:
    lcd.clear()  # Clear the entire LCD before displaying the "Exiting..." message
    lcd.cursor_pos = (0, 0)  # Set cursor to the beginning of the first line
    lcd.write_string("Exiting...")
    GPIO.output(led_pin, GPIO.LOW)  # Turn off the LED
    time.sleep(2)  # Wait for 2 seconds to show the "Exiting..." message
    lcd.clear()  # Clear the LCD again before exiting the program
    GPIO.cleanup()  # Cleanup GPIO configuration
    sys.exit(0)
