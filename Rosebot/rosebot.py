import gpiozero as gz

class Rosebot:
    def __init__(self):
            self.drive_system = None
            self.leds = None
            self.ultrasonic = None
            self.line_sensors = None
            self.servo_head = None # might not actually get made
            self.buzzer = gz.Buzzer(17)
            self.adc = None




