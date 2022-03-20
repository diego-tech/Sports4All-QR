# Librerias
import RPi.GPIO as GPIO
import time

# Variables
green_led_pin = 7
red_led_pin = 25
buzzer_pin = 15

# Funciones


def setPines():
    # Set Pines
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(green_led_pin, GPIO.OUT)
    GPIO.setup(red_led_pin, GPIO.OUT)
    GPIO.setup(buzzer_pin, GPIO.OUT)


def sensorOn():
    setPines()
    GPIO.output(green_led_pin, GPIO.HIGH)
    GPIO.output(red_led_pin, GPIO.LOW)
    time.sleep(1)


def sensorOff():
    setPines()
    GPIO.output(green_led_pin, GPIO.HIGH)
    GPIO.output(red_led_pin, GPIO.HIGH)
    time.sleep(1)

def buzzerOn():
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(buzzer_pin, GPIO.LOW)

