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
            let res = this.fetchGuestId();
            if(res=='ok'){

                await axios.post(`http://localhost:5000/guests/bookings/${this.guest_id}/${property_id}`)
                    .then(response => {
                        alert(`Property Booked successfully. Property ID: ${response.data.booking_id}`);
                    })
                    .catch(error => {
                        alert(`Error: ${error.response.data.error}`);
                    });
                
                window.location.reload();
            }

        },
        fetchGuestId() {
            // parsing localstorage data
            const credentials = JSON.parse(localStorage.getItem('credentials'));
            if (credentials) {
                const email = credentials['email'];
                const role = credentials['role'];
                if (role == "host") {
                    alert("Host not allowed to book")
                    return "not"
                } else {
                    axios
                        .get(`http://localhost:5000/guestemail/${email}`)
                        .then(response => {
                            this.propertyData.guest_id = response.data.guest_id;
                            return "ok"
                        })
                        .catch(error => {
                            alert(`Error: ${error.response.data.error}`);
                            window.location = '/login'
                            return "not"
                        });
                }
            } else {
                alert("Please login...")
                window.location = '/login'
                return "not"
            }

        }

    },
    

}
</script>
    
<style scoped>

#cont h1{
    text-align: center;
}
.prop {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 10px;
}
.prop h3{
    
    margin: 0;
}
.prop h4{
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
    