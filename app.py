from flask import Flask, render_template, jsonify, request
import RPi.GPIO as GPIO
import math
from Controller.Stepper import move
from Global.Configuration import Configuration
from Util.StepperUtilities import map_range

# Initialize config singleton
config = Configuration()

# Initialize Flask app
app = Flask(__name__)

############################################################
############################################################
############################################################

# Endpoint for UI controls
@app.route('/')
def index():
    return render_template('./gpt.html')

############################################################
############################################################
############################################################

# Endpoint for triggering stepper motor movement
@app.route('/run', methods=['POST'])
def run():
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
    move(mapped_speed, revolutions, 1 if direction_ccw else 0)
    
    # Reset stop flag
    config.set_stop(False)
    
    response_data = {
        'message': 'Data received and processed successfully',
        'speed': mapped_speed,
        'direction_cw': direction_cw,
        'direction_ccw': direction_ccw,
        'revolutions': revolutions
    }
    return jsonify(response_data)

############################################################
############################################################
############################################################

# Endpoint for Stopping stepper motor movement
@app.route('/stop', methods=['GET'])
def stop_route():
    config.set_stop(True)
    return jsonify({'message': 'Stop action initiated'})

############################################################
############################################################
############################################################

if __name__ == '__main__':
    config.set_limit_right(False)
    config.set_limit_left(False)
    app.run(debug=True, host='0.0.0.0', port=8000)
