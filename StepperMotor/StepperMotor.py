import RPi.GPIO as GPIO
import time
from threading import Thread
from Global.Configuration import Configuration

# Initialize configuration singleton
config = Configuration()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class StepperMotor:
    def __init__(self, lad, lasp, lae, lsi):
        self._initialize(lad, lasp, lae, lsi)

    def _initialize(self, lad, lasp, lae, lsi):
        self.LinearActuatorDir = lad  # yellow
        self.LinearActuatorStepPin = lasp  # white
        self.LinearActuatorEnable = lae  # black/green
        self.LimitSwitchInput = lsi  # 36

        self.limitRight = False
        self.limitLeft = False
        self.stop = False

        GPIO.setup(self.LinearActuatorDir, GPIO.OUT)
        GPIO.setup(self.LinearActuatorStepPin, GPIO.OUT)
        GPIO.setup(self.LinearActuatorEnable, GPIO.OUT)
        GPIO.setup(self.LimitSwitchInput, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(self.LinearActuatorEnable, GPIO.HIGH)

        # Spin off thread for listening to limit switch
        self.limit_switch_thread = Thread(target=self.listen_for_limit_switch)
        self.limit_switch_thread.daemon = True
        self.limit_switch_thread.start()

    def move(self, speed, rev=1, dir=0):
        GPIO.output(self.LinearActuatorDir, dir)
        for i in range(rev * config.get_steps_per_revolution()):
            if self.stop or (self.limitRight and dir == 0) or (self.limitLeft and dir == 1) or config.get_stop():
                break
            GPIO.output(self.LinearActuatorStepPin, 1)
            time.sleep(speed)
            GPIO.output(self.LinearActuatorStepPin, 0)
            time.sleep(speed)

    def set_limit_left(self, val):
        self.limitLeft = val
    
    def set_limit_right(self, val):
        self.limitRight = val
    
    def set_stop(self, val):
        self.stop = val

    def listen_for_limit_switch(self):
        try:
            while True:
                current_state = GPIO.input(self.LimitSwitchInput)
                if current_state == GPIO.LOW:
                    self.limitRight = True
                else:
                    self.limitRight = False
                time.sleep(0.01)
        finally:
            GPIO.cleanup()

# Example usage:
# motor = StepperMotor(lad=11, lasp=12, lae=13, lsi=15)  # GPIO pin numbers
# motor.move(speed=0.01, rev=10, dir=0)
