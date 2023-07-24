<template>
    <div id="cont">
        <h1>My Bookings</h1>
        <div class="prop">
            <div v-for="property in properties" :key="property">

                <img :src="property.image" :alt="property.name">
                <h3>{{ property.name }}</h3>
                <h4>{{ property.location }}</h4>
                <p>Price: ₹{{ property.price }}</p>

                <button class="hoverGreen" v-on:click="checkout(property._id)">Checkout</button>
                <p class="red">{{ property.status == "Booked" ? "Booked" : "" }}</p>

            </div>
        </div>
    </div>
</template>
    
<script>
import axios from 'axios';
import Swal from 'sweetalert2';
export default {
    name: 'BookingComp',
    data() {
        return {
            properties: [],
            guest_id: '',
            baseUrl: 'https://vacation-rental-backend-ten.vercel.app/'
        }
    },
    async mounted() {
        await this.fetchGuestId(); // to load guest id
        await axios.get(this.baseUrl+'properties')
            .then(response => {
                const myBookings = response.data.filter((property) => property['guest_id'] == this.guest_id)
                this.properties = myBookings;
            })
            .catch(error => {
                console.log(error.response)
            })

    },
    methods: {

        async checkout(property_id) {
            try {
                const result = await Swal.fire({
                    title: 'Are you sure?',
                    text: "You won't be able to revert this!",
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Yes'
                });

                if (result.isConfirmed) {
                    // Fetch the guest ID
                    const res = await this.fetchGuestId();

                    if (res === "ok") {
                        // Guest ID fetched successfully, proceed with booking
                        const response = await axios.delete(`${this.baseUrl}guests/checkout/${this.guest_id}/${property_id}`);

                        // Show success message and reload the page
                        await Swal.fire({
                            title: response.data.message,
                            // text: response.data.message,
                            icon: 'success',
                            showConfirmButton: true, // Remove the 'OK' button
                            confirmButtonText: 'OK',
                        });

                        window.location.reload();
                    }
                }
            } catch (error) {
                // Handle any errors that occurred during the booking process
                if (error.response && error.response.data && error.response.data.error) {
                    // Display the specific error message from the server response
                    alert(`Error: ${error.response.data.error}`);
                } else {
                    // Display a generic error message
                    alert("An error occurred. Please try again later.");
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
                    alert("Host not allowed");
                    return "not";
                } else {
                    // Fetch guest ID from the server
                    try {
                        const response = await axios.get(`${this.baseUrl}guestemail/${email}`);
                        this.guest_id = response.data.guest_id;
                        return "ok";
                    } catch (error) {
                        alert(`Error: ${error.message}`);
                        window.location = '/login';
                        return "not";
                    }
                }
            } else {
                // Guest is not logged in
                alert("Please login...");
                window.location = '/login';
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
#cont {
    margin-bottom: 50px;
    padding: 2.5%;
}

.prop {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 10px;
    

}
.prop div{
    transition: 0.3s;
}
.prop div:hover{
    transform: scale(0.98);
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
    padding: 5px 10px;
}

.hoverRed:hover {
    color: red;
}

.hoverGreen:hover {
    color: green;
    border: 2px solid transparent;
    border-image: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
    border-image-slice: 1;
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
    