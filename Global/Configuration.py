class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.LinearActuatorDir = 5
        self.LinearActuatorStepPin = 3
        self.LinearActuatorEnable = 7
        self.LimitSwitchInput = 36

        self.StepsPerRevolution = 800
        self.FastSpeed = 0.0000375  # 0.00035
        self.LowSpeed = 0.001  # 0.0003125

        self.limitRight = False
        self.limitLeft = False

        self.stop = False

    def get_linear_actuator_dir(self):
        return self.LinearActuatorDir

    def set_linear_actuator_dir(self, value):
        self.LinearActuatorDir = value

    def get_linear_actuator_step_pin(self):
        return self.LinearActuatorStepPin

    def set_linear_actuator_step_pin(self, value):
        self.LinearActuatorStepPin = value

    def get_linear_actuator_enable(self):
        return self.LinearActuatorEnable

    def set_linear_actuator_enable(self, value):
        self.LinearActuatorEnable = value

    def get_limit_switch_input(self):
        return self.LimitSwitchInput

    def set_limit_switch_input(self, value):
        self.LimitSwitchInput = value

    def get_steps_per_revolution(self):
        return self.StepsPerRevolution

    def set_steps_per_revolution(self, value):
        self.StepsPerRevolution = value

    def get_fast_speed(self):
        return self.FastSpeed

    def set_fast_speed(self, value):
        self.FastSpeed = value

    def get_low_speed(self):
        return self.LowSpeed

    def set_low_speed(self, value):
        self.LowSpeed = value

    def get_limit_right(self):
        return self.limitRight

    def set_limit_right(self, value):
        self.limitRight = value

    def get_limit_left(self):
        return self.limitLeft

    def set_limit_left(self, value):
        self.limitLeft = value

    def get_stop(self):
        return self.stop

    def set_stop(self, value):
        self.stop = value