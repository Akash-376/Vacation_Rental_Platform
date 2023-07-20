<template>
    <div id="cont">
        <h1>All Properties</h1>
        <div class="prop">
            <div v-for="property in properties" :key="property">

                <img :src="property.image" :alt="property.name">
                <h3>{{ property.name }}</h3>
                <h4>{{ property.location }}</h4>
                <p>Price: ₹{{ property.price }}</p>

                <button class="hoverGreen" v-on:click="bookProperty(property._id)">book now</button>
                <p class="red">{{ property.status == "Booked" ? "Booked" : "" }}</p>

            </div>
        </div>
    </div>
</template>
    
<script>
import axios from 'axios';
import Swal from 'sweetalert2';
export default {
    name: 'PropertyComp',
    data() {
        return {
            properties: [],
            guest_id: ''
        }
    },
    async mounted() {
        await axios.get('http://127.0.0.1:5000/properties')
            .then(response => {
                this.properties = response.data;
            })
        // console.warn("Api data : ", result.data);

    },
    methods: {

        async bookProperty(property_id) {
            try {
                // Fetch the guest ID
                let res = await this.fetchGuestId();  // fetchGuestId() this method retuen a promise

                if (res === "ok") {
                    // Guest ID fetched successfully, proceed with booking
                    let result = await axios.post(`http://localhost:5000/guests/bookings/${this.guest_id}/${property_id}`);

                    // Show success message and reload the page

                    Swal.fire({
                        title: 'Congratulations! Booking successful',
                        text: 'Booking ID: ' + result.data.booking_id,
                        icon: 'success',
                        showConfirmButton: true, // Remove the 'OK' button
                        confirmButtonText: 'OK',
                        
                    }).then(result => {
                        if(result.isConfirmed){
                            window.location.reload();
                        }
                    })
                }
            } catch (error) {
                // Handle any errors that occurred during the booking process
                if (error.response && error.response.data && error.response.data.error) {
                    // Display the specific error message from the server response

                    Swal.fire({
                        title: 'Oops...',
                        text: error.response.data.error,
                        icon: 'error',
                        showConfirmButton: true,
                        confirmButtonText: 'OK',

                    })
                    // alert(`Error: ${error.response.data.error}`);
                } else {
                    // Display a generic error message
                    Swal.fire({
                        title: 'Oops...',
                        text: `Something went wrong!`,
                        icon: 'error',
                        showConfirmButton: true,
                        confirmButtonText: 'Try again',

                    })

                    // alert("An error occurred. Please try again later.");
                }
            }
        },

        async fetchGuestId() {
            // Parsing local storage data to get guest's email
            const credentials = JSON.parse(localStorage.getItem('credentials'));
            if (credentials) {
                const email = credentials.email;
                const role = credentials.role;

                if (role === "host") {
                    // Host is not allowed to book
                    Swal.fire({
                        title: 'Oops...',
                        text: `Host not allowed to book`,
                        icon: 'error',
                        showConfirmButton: true,
                        confirmButtonText: 'Try again',

                    })
                    return "not";
                } else {
                    // Fetch guest ID from the server
                    try {
                        const response = await axios.get(`http://localhost:5000/guestemail/${email}`);
                        this.guest_id = response.data.guest_id;
                        return "ok";
                    } catch (error) {

                        Swal.fire({
                            title: 'Oops...',
                            text: error.message,
                            icon: 'error',
                            showConfirmButton: true,
                            confirmButtonText: 'Try again',

                        }).then(result => {
                            if (result.isConfirmed) window.location = '/login';
                        })
                        return "not";
                    }
                }
            } else {
                // Guest is not logged in
                Swal.fire({
                    title: 'Oops...',
                    text: 'Please login...',
                    icon: 'error',
                    showConfirmButton: true,
                    confirmButtonText: 'Try again',

                }).then(result => {
                    if (result.isConfirmed) window.location = '/login';
                })
                return "not";
            }
        },

    },


}
</script>
    
<style scoped>
#cont h1 {
    text-align: center;
}

.prop {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 20px;
}
.prop div{
    margin-bottom: 50px;
}

.prop h3 {

    margin: 0;
}

.prop h4 {
    color: grey;
    margin: 4px;

}

img {
    width: 100%;
    height: 70%;
    margin-bottom: 10px;
}

p {
    margin: 4px;


}

.red {
    color: red;
}

button {
    cursor: pointer;
    font-size: 20px;
    margin-top: 10px;
}

.hoverRed:hover {
    color: red;
}

.hoverGreen:hover {
    color: green;
    border: 2px solid #333;
}

.hoverOrange {
    text-decoration: none;
    color: black;
}

.hoverOrange:hover {
    color: orange;
    text-decoration: none;
}
</style>
    