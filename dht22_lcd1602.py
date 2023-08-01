{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from RPLCD.i2c import CharLCD\
import Adafruit_DHT\
import time\
import sys\
\
# Replace 0x27 with the I2C address of your LCD module\
lcd = CharLCD('PCF8574', 0x27)\
\
# Set the sensor type and the GPIO pin\
sensor = Adafruit_DHT.DHT22\
pin = 4  # Replace 4 with the actual GPIO pin number you've connected the DHT22 to\
\
try:\
    while True:\
        # Attempt to get sensor reading\
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)\
\
        # Display readings on the LCD if they are valid\
        if humidity is not None and temperature is not None:\
            lcd.cursor_pos = (0, 0)  # Set cursor to the beginning of the first line\
            lcd.write_string(f"Temp: \{temperature:.2f\}C")\
            lcd.cursor_pos = (1, 0)  # Set cursor to the beginning of the second line\
            lcd.write_string(f"Humi: \{humidity:.2f\}%")\
        else:\
            lcd.clear()  # Clear the LCD in case of invalid data\
            lcd.write_string("Failed to retrieve\\nsensor data")\
\
        time.sleep(2)  # Wait for a few seconds before taking another reading\
\
except KeyboardInterrupt:\
    lcd.clear()  # Clear the entire LCD before displaying the "Exiting..." message\
    lcd.cursor_pos = (0, 0)  # Set cursor to the beginning of the first line\
    lcd.write_string("Exiting...")\
    time.sleep(2)  # Wait for 2 seconds to show the "Exiting..." message\
    lcd.clear()  # Clear the LCD again before exiting the program\
    sys.exit(0)\
}