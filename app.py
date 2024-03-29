from flask import Flask, render_template, jsonify, request
import RPi.GPIO as GPIO
import math
# from Controller.Stepper import move
from Global.Configuration import Configuration
from Util.StepperUtilities import map_range
from StepperMotor.StepperMotor import StepperMotor
from threading import Thread

# Initialize config singleton
config = Configuration()

#Initialize stepper motor instances and move methods
railStepperMotor = StepperMotor(5,3,7,8)
beltStepperMotor = StepperMotor(36,38,40,8)

def move_rail_motor(mapped_speed, revolutions, direction_ccw):
    railStepperMotor.move(mapped_speed, revolutions, 1 if direction_ccw else 0)

def move_belt_motor(mapped_speed, revolutions, direction_ccw):
    beltStepperMotor.move(mapped_speed, revolutions, 1 if direction_ccw else 0)

def move_motor(motor, mapped_speed, revolutions, direction_ccw):
    motor.move(mapped_speed, revolutions, 1 if direction_ccw else 0)

# Initialize Flask app
app = Flask(__name__)

############################################################
############################################################
############################################################

# Endpoint for UI controls
@app.route('/')
def index():
    return render_template('./multiple.html')

############################################################
############################################################
############################################################


def run(motor, request):
    # Get JSON data from the request body
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ['speed', 'directionCW', 'directionCCW', 'revolutions']):
        return jsonify({'error': 'Missing required fields in request data'}), 400

    try:
        speed = int(data['speed'])
        direction_cw = bool(data['directionCW'])
        direction_ccw = bool(data['directionCCW'])
        revolutions = int(data['revolutions'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid data types in request data'}), 400

    # Map speed and trigger movement of stepper motor
    mapped_speed = map_range(speed, 1, 1000, config.get_low_speed(), config.get_fast_speed())

    # Create threads for each motor for simultaneous movement
    motor_thread = Thread(target=move_motor, args=(motor, mapped_speed, revolutions, direction_ccw))
    motor_thread.start()
    motor_thread.join()

    # Reset stop flag
    # config.set_stop(False)
    motor.set_stop(False)
    
    response_data = {
        'message': 'Data received and processed successfully',
        'speed': mapped_speed,
        'direction_cw': direction_cw,
        'direction_ccw': direction_ccw,
        'revolutions': revolutions
    }
    return jsonify(response_data)

# Endpoints for triggering stepper motor movement
@app.route('/run-m1', methods=['POST'])
def runm1():
    return run(railStepperMotor, request)

@app.route('/run-m2', methods=['POST'])
def runm2():
    return run(beltStepperMotor, request)

############################################################
############################################################
############################################################

# Endpoint for Stopping stepper motor movement
@app.route('/stop-m1', methods=['GET'])
def stop_routem1():
    # config.set_stop(True)
    railStepperMotor.set_stop(True)
    return jsonify({'message': 'Stop action initiated'})

@app.route('/stop-m2', methods=['GET'])
def stop_routem2():
    # config.set_stop(True)
    beltStepperMotor.set_stop(True)
    return jsonify({'message': 'Stop action initiated'})

############################################################
############################################################
############################################################

if __name__ == '__main__':
    railStepperMotor.set_limit_right(False)
    railStepperMotor.set_limit_left(False)

    beltStepperMotor.set_limit_right(False)
    beltStepperMotor.set_limit_left(False)
    
    # config.set_limit_right(False)
    # config.set_limit_left(False)

    app.run(debug=True, host='0.0.0.0', port=8000)
