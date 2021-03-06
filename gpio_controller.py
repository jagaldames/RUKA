import RPi.GPIO as GPIO
import gpio_variables as v


class GPIOController:
    button_pin = v.button_pin
    led_pin = v.led_pin
    switch_pin = v.switch_pin

    initialized = False

    def __init__(self):
        if GPIOController.initialized:
            print('Warning: GPIO already initialized.')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(GPIOController.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(GPIOController.switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(GPIOController.led_pin, GPIO.OUT)
        GPIO.output(GPIOController.led_pin, False)
        GPIOController.initialized = True

    @staticmethod
    def cleanup():
        GPIO.cleanup()

    @staticmethod
    def block_until_press():
        if not GPIOController.initialized:
            raise RuntimeError('GPIO not initialized.')
        while True:
            state = GPIO.input(GPIOController.button_pin)
            if not state:
                return

    @staticmethod
    def set_led(state):
        if not GPIOController.initialized:
            raise RuntimeError('GPIO not initialized.')
        GPIO.output(GPIOController.led_pin, state)

    @staticmethod
    def get_switch():
        if not GPIOController.initialized:
            raise RuntimeError('GPIO not initialized.')
        state = GPIO.input(GPIOController.switch_pin)
        return state
