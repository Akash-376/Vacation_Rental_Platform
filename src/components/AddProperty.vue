<template>
    <div id="body">


        <div id="container">
            <h1>Register Property</h1>
            <form @submit.prevent="registerProperty">
                <label for="propertyName">Property Name</label>
                <input type="text" id="propertyName" v-model="propertyData.name" required>

                <label for="image">Property image</label>
                <input type="url" id="image" v-model="propertyData.image" required>

                <label for="location">Location</label>
                <select id="location" v-model="propertyData.location" required>
                    <option disabled value="">Choose location</option>
                    <option value="Chandigarh">Chandigarh</option>
                    <option value="Delhi">Delhi</option>
                    <option value="Haryana">Haryana</option>
                    <option value="Goa">Goa</option>
                    <option value="Gujarat">Gujarat</option>
                    <option value="Himachal Pradesh">Himachal Pradesh</option>
                    <option value="Jammu and Kashmir">Jammu and Kashmir</option>
                    <option value="Ladakh">Ladakh</option>
                    <option value="Puducherry">Puducherry</option>
                    <option value="Punjab">Punjab</option>
                    <option value="Rajasthan">Rajasthan</option>
                    <option value="Uttar Pradesh">Uttar Pradesh</option>
                    <option value="Uttarakhand">Uttarakhand</option>
                </select>


                <label for="propertyType">Property Type:</label>
                <select id="propertyType" v-model="propertyData.property_type" required>
                    <option disabled value="">Choose property type</option>
                    <option value="Apartment">Apartment</option>
                    <option value="House">House</option>
                    <option value="Unique Homes">Unique Homes</option>
                </select>

                <label for="description">Description:</label>
                <textarea id="description" v-model="propertyData.description" required></textarea>


                <label for="price">Price:</label>
                <input id="price" v-model="propertyData.price" required>

                <button type="submit">Register</button>
            </form>
        </div>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    name: 'AddPropertyComp',
    data() {
        return {
            propertyData: {
                host_id: '',
                name: '',
                image: '',
                location: '',
                property_type: '',
                description: '',
                price: '',
            },
        };
    },
    methods: {
        async registerProperty() {
            const res = await this.fetchHostId();
            if (res === 'ok') {
                axios
                    .post('http://localhost:5000/properties', this.propertyData)
                    .then((response) => {
                        alert(`Property added successfully. Property ID: ${response.data.property_id}`);
                    })
                    .catch((error) => {
                        alert(`Error: ${error.response.data.error}`);
                    });
            }
        },
        async fetchHostId() {
            // parsing localstorage data
            const credentials = JSON.parse(localStorage.getItem('credentials'));

            if (credentials) {
                const email = credentials['email'];
                const role = credentials['role'];

                if (role === 'guest') {
                    alert("Guests are not allowed to add properties");
                    return 'not';
                } else {
                    try {
                        const response = await axios.get(`http://localhost:5000/hostemail/${email}`);
                        this.propertyData.host_id = response.data.host_id;
                        return 'ok'; // Correctly returning 'ok' if host ID is fetched successfully
                    } catch (error) {
                        alert(`Error: ${error.response.data.error}`);
                        return 'not';
                    }
                }
            } else {
                alert('Please login...');
                window.location = '/login';
                return 'not';
            }
        },
    },
};
</script>

<style scoped>
#body {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 89vh;
    background-image: url('https://media.istockphoto.com/id/104731717/photo/luxury-resort.jpg?s=612x612&w=0&k=20&c=cODMSPbYyrn1FHake1xYz9M8r15iOfGz9Aosy9Db7mI=');
    background-size: cover;
    background-position: center;
}

#container {
    width: 33%;
    padding: 20px;
    background-color: #f0f0f0;
    border-radius: 5px;
    margin: auto;
}

h1 {
    text-align: center;
    margin-bottom: 20px;
}

label {
    display: block;
    font-weight: bold;
    margin-top: 10px;
}

input,
select,
textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 5px;
}

button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #4caf50;
    color: #fff;
    font-weight: bold;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    background-color: #45a049;
}
</style>