import RPi.GPIO as GPIO
import time

# Ustawienie trybu numerowania pinów
GPIO.setmode(GPIO.BCM)

# Wybór pinu, do którego podłączona jest dioda LED
led_pin = 18

# Ustawienie pinu jako wyjście
GPIO.setup(led_pin, GPIO.OUT)

# Pętla migająca LED-em
try:
    while True:
        # Zaświecenie LED
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
        
        # Czekanie 1 sekundę
        time.sleep(0.1)
        
        # Zgaszenie LED
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")
        
        # Czekanie 1 sekundę
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program został przerwany")

# Czyszczenie ustawień GPIO po zakończeniu programu
GPIO.cleanup()
