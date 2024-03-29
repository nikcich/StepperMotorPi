class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Track
        # self.LinearActuatorDir = 5 # yellow
        # self.LinearActuatorStepPin = 3 # white
        # self.LinearActuatorEnable = 7 # black/green

        # Belt
        # self.LinearActuatorDir = 36 # yellow
        # self.LinearActuatorStepPin = 38 # white
        # self.LinearActuatorEnable = 40 # black/green

        # self.LimitSwitchInput = 8 # 36

        self.StepsPerRevolution = 800
        self.FastSpeed = 0.0000375  # 0.00035
        self.LowSpeed = 0.001  # 0.0003125

        self.stop = False

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

    def get_stop(self):
        return self.stop

    def set_stop(self, value):
        self.stop = value