import RPi.GPIO as GPIO
import time
from threading import Thread
from Global.Configuration import Configuration

# Initialize configuration singleton
config = Configuration()

############################################################
############################################################
############################################################

# Initialize GPIO settings
# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(config.get_linear_actuator_dir(), GPIO.OUT)
# GPIO.setup(config.get_linear_actuator_step_pin(), GPIO.OUT)
# GPIO.setup(config.get_linear_actuator_enable(), GPIO.OUT)
# GPIO.setup(config.get_limit_switch_input(), GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set up pin with pull-up resistor
# GPIO.output(config.get_linear_actuator_enable(), GPIO.HIGH)

# ############################################################
# ############################################################
# ############################################################

# def move(speed, rev=1, dir=0):
#     print(config.get_stop(), config.get_limit_right(), config.get_limit_left(), dir)

#     GPIO.output(config.get_linear_actuator_dir(), dir)
#     for i in range(rev * config.get_steps_per_revolution()):
#         if config.get_stop() or (config.get_limit_right() and dir == 0) or (config.get_limit_left() and dir == 1):
#             break
#         GPIO.output(config.get_linear_actuator_step_pin(), 1)
#         time.sleep(speed)
#         GPIO.output(config.get_linear_actuator_step_pin(), 0)
#         time.sleep(speed)

# ############################################################
# ############################################################
# ############################################################ 

# def listenForLimitSwitch():
#     try:
#         while True:
#             current_state = GPIO.input(config.get_limit_switch_input())
#             if current_state == GPIO.LOW:
#                 config.set_limit_right(True)
#             else:
#                 config.set_limit_right(False)
#             time.sleep(0.01)
#     finally:
#         GPIO.cleanup()

# ############################################################
# ############################################################
# ############################################################

# # Spin off thread for listening to limit switch
# limit_switch_thread = Thread(target=listenForLimitSwitch)
# limit_switch_thread.daemon = True
# limit_switch_thread.start()
