import RPi.GPIO as GPIO
import time

# Ustawienie trybu numerowania pinów
GPIO.setmode(GPIO.BCM)

# Wybór pinu, do którego podłączona jest dioda LED
led_pin = 18

# Ustawienie pinu jako wyjście
GPIO.setup(led_pin, GPIO.OUT)

# Zaświecenie LED
GPIO.output(led_pin, GPIO.HIGH)

print("LED is ON")

# Czekanie 5 sekund
time.sleep(5)

# Zgaszenie LED
GPIO.output(led_pin, GPIO.LOW)

# Czekanie 5 sekund
time.sleep(5)

# Zaświecenie LED
GPIO.output(led_pin, GPIO.HIGH)

# Zgaszenie LED
GPIO.output(led_pin, GPIO.LOW)

# Czekanie 5 sekund
time.sleep(5)

# Zaświecenie LED
GPIO.output(led_pin, GPIO.HIGH)

# Zgaszenie LED
GPIO.output(led_pin, GPIO.LOW)

# Czekanie 5 sekund
time.sleep(5)

# Zaświecenie LED
GPIO.output(led_pin, GPIO.HIGH)

# Zgaszenie LED
GPIO.output(led_pin, GPIO.LOW)

# Czekanie 5 sekund
time.sleep(5)

# Zaświecenie LED
GPIO.output(led_pin, GPIO.HIGH)

# Zgaszenie LED
GPIO.output(led_pin, GPIO.LOW)



print("LED is OFF")

# Czyszczenie ustawień GPIO
GPIO.cleanup()