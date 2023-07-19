

from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson import ObjectId
from flask_cors import CORS # to handle CORS policy error

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
client = MongoClient('mongodb://localhost:27017/')
db = client['hotel_renting']







# Entity1: Host
#Register Host
@app.route('/hosts', methods=['POST'])
def create_host():
    data = request.json
    email = data.get('email')
    # print(email)

    # Check if email already exists
    existing_host = db.hosts.find_one({'email': email})
    if existing_host:
        return jsonify({'error': 'This Email is already registered. Please try with another one'}), 400

    host_id = db.hosts.insert_one(data).inserted_id
    return jsonify({'host_id': str(host_id)}), 201

# get host by Id
@app.route('/hosts/<host_id>', methods=['GET'])
def get_host(host_id):
    host = db.hosts.find_one({'_id': ObjectId(host_id)})
    if host:
        host["_id"] = str(host["_id"])
        return jsonify(host), 200
    else:
        return jsonify({'error': 'Host not found'}), 404

# Implement routes for updating and deleting hosts






# Entity2: Property

# create new property
@app.route('/properties', methods=['POST'])
def create_property():
    data = request.json
    data['status'] = 'Available'  # Set the initial status to 'Available'
    host_id = data.get('host_id')

    # Check if the host_id is not provided or is empty
    if not host_id:
        return jsonify({'error': 'Host ID is required'}), 400

    # Check if the host exists
    host = db.hosts.find_one({'_id': ObjectId(host_id)})
    if not host:
        return jsonify({'error': 'Host not found'}), 404

    # Insert the property document
    property_id = db.properties.insert_one(data).inserted_id

    # Add the property ID to the host's properties field
    db.hosts.update_one({'_id': ObjectId(host_id)}, {'$push': {'properties': property_id}})

    return jsonify({'property_id': str(property_id)}), 201

# get property by Id
@app.route('/properties/<property_id>', methods=['GET'])
def get_property(property_id):
    property = db.properties.find_one({'_id': ObjectId(property_id)})
    if property:
        property["_id"] = str(property["_id"])
        return jsonify(property), 200
    else:
        return jsonify({'error': 'Property not found'}), 404

# Implement routes for updating and deleting properties






# Entity3: Guest

# Register new guest
@app.route('/guests', methods=['POST'])
def create_guest():
    data = request.json
    guest_id = db.guests.insert_one(data).inserted_id
    return jsonify({'guest_id': str(guest_id)}), 201


# get guest by Id
@app.route('/guests/<guest_id>', methods=['GET'])
def get_guest(guest_id):
    guest = db.guests.find_one({'_id': ObjectId(guest_id)})
    if guest:
        guest["_id"] = str(guest["_id"])
        return jsonify(guest), 200
    else:
        return jsonify({'error': 'Guest not found'}), 404


# Guest booking route
@app.route('/guests/bookings/<guest_id>/<property_id>', methods=['POST'])
def book_property(guest_id, property_id):
    # data = request.json
    # property_id = data.get('property_id')
    guest = db.guests.find_one({'_id': ObjectId(guest_id)})
    property = db.properties.find_one({'_id': ObjectId(property_id)})

    if guest and property and property['status'] == 'Available':
        
        # Create booking document
        booking_data = {
            'guest_id': guest_id,
            'property_id': property_id
        }
        booking_id = db.bookings.insert_one(booking_data).inserted_id

        # Update property status to 'Booked'
        db.properties.update_one({'_id': ObjectId(property_id)}, {'$set': {'status': 'Booked'}})

        return jsonify({'booking_id': str(booking_id)}), 201
    # if property is already booked
    elif guest and property and property['status'] == 'Booked':
        return jsonify({'message': 'This property is already booked. Please try another one...'}), 200
    else:
        return jsonify({'error': 'Guest or Property not found or Property is not available'}), 404


# Guest checkout route
@app.route('/guests/checkout/<booking_id>', methods=['DELETE'])
def checkout(booking_id):
    # guest = db.guests.find_one({'_id': ObjectId(guest_id)})
    booking = db.bookings.find_one({'_id': ObjectId(booking_id)})
    # print(guest_id)
    print(booking_id)

    if booking:
        # Delete the booking document
        db.bookings.delete_one({'_id': ObjectId(booking_id)})

        property_id = booking['property_id']

        # Update property status to 'Available'
        db.properties.update_one({'_id': ObjectId(property_id)}, {'$set': {'status': 'Available'}})

        return jsonify({'message': 'Checkout successful'}), 200
    else:
        return jsonify({'error': 'Booking details not found'}), 404

# Implement routes for updating and deleting guests





            #BOOKING





# Entity4: Booking

# NO need to create Booking manually it will be created automatically when customer will book ant property


# Implement routes for updating and deleting bookings




if __name__ == '__main__':
    app.run(debug=True)