from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

# Define the CSV file path
CSV_FILE = 'timestamps.csv'

# Initialize the CSV file with headers if it doesn't exist
def init_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['timestamp'])
    except FileExistsError:
        pass

@app.route('/post_timestamp', methods=['POST'])
def post_timestamp():
    data = request.get_json()
    timestamp = data.get('timestamp')
    
    if timestamp:
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp])
        
        return jsonify({'message': 'Timestamp successfully written to CSV'}), 200
    else:
        return jsonify({'error': 'No timestamp provided'}), 400

if __name__ == '__main__':
    init_csv()  # Ensure the CSV file exists
    app.run(debug=True)
