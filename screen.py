import time
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

# Konfoguracja wyświetlacza LCD

lcd = CharLCD(
    pin_rs=26, pin_rw=None, pin_e=19,
    pins_data=[13, 6, 5, 11],
    numbering_mode=GPIO.BCM,
    cols=16, rows=2
)

def main():
    lcd.clear()
    lcd.write_string("Nasz wyswietlacz")
    lcd.cursor_pos = (1, 0) # Przejście do drugiego wiersza
    lcd.write_string("dziala!")

    # Utrzymanie komunikatu przez 15s
    time.sleep(15)

    # czyścimy komunikat
    lcd.clear()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        lcd.clear()
        lcd.write_string("Program zakonczony")
        GPIO.cleanup()