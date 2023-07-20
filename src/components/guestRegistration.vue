<template>
    <div id="body">


        <div id="container">
            <h1>Guest Signup</h1>
            <form @submit.prevent="registerGuest">
                <label for="name">Name</label>
                <input type="text" id="name" v-model="guestData.name" required>

                <label for="email">Email</label>
                <input type="email" id="email" v-model="guestData.email" required>

                <label for="mobile">Mobile</label>
                <input type="text" id="mobile" v-model="guestData.mobile" required>

                <label for="password">Password</label>
                <input type="password" id="password" v-model="guestData.password" required>

                <label for="address">Address</label>
                <input type="text" id="address" v-model="guestData.address" required>


                <label for="gender">Gender</label>
                <div class="radio">

                    <div>
                        <input type="radio" id="male" value="Male" v-model="guestData.gender">
                        <label for="male">Male</label>
                    </div>
                    <div>
                        <input type="radio" id="female" value="Female" v-model="guestData.gender">
                        <label for="female">Female</label>
                    </div>

                </div>
                <label for="dob">Date of Birth</label>
                <input type="date" id="dob" v-model="guestData.dob" :max="getCurrentDate()" required>


                <label for="about">Bio</label>
                <textarea id="about" v-model="guestData.about" required></textarea>

                <button type="submit">Register</button>
            </form>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios'
import Swal from 'sweetalert2';
export default {
    name: "RegisterGuestComp",
    data() {
        return {
            guestData: {
                name: "",
                mobile: "",
                email: "",
                password: "",
                address: "",
                gender: "",
                about: "",
                dob: ""

            }
        };
    },
    methods: {
        registerGuest() {

            axios.post('http://localhost:5000/guests', this.guestData)
                .then(response => {
                    // Handle the response from the server
                    // Optionally, you can display a success message or redirect to a different page
                    const guestId = response.data.guest_id;

                    Swal.fire({
                        title: 'Registration successful !',
                        text: "Added! with guest ID " + guestId,
                        icon: 'success',
                        showConfirmButton: false, // Remove the 'OK' button
                        timer: 2000, // Set the timer for 2 seconds (adjust as needed)
                        willClose: () => {
                            window.location = '/'; // Redirect after the animation completes
                        }
                    });

                    // alert("Added! with guest ID "+ guestId)
                    // window.location = '/'
                })
                .catch(error => {
                    // Handle any errors that occurred during the registration process
                    // Optionally, you can display an error message to the user

                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: error.response.data.error,
                        footer: '<a href="">go to home page</a>'
                    })
                    // alert(error.response.data.error)
                });
        },
        getCurrentDate() {
            const today = new Date();
            const year = today.getFullYear() - 15; // to prevent rent house below 15 years old guys
            let month = today.getMonth() + 1;
            let day = today.getDate();

            if (month < 10) {
                month = `0${month}`;
            }
            if (day < 10) {
                day = `0${day}`;
            }

            return `${year}-${month}-${day}`;
        }
    }
};
</script>

<style scoped>
/* #body {
    background-image: url('https://images7.alphacoders.com/436/436350.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
} */
#container {
    width: 40%;
    margin: 10px auto;
    padding: 20px;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
    background-color: white;

}

#container h1 {
    text-align: center;
    font-size: 30px;
}

h1 {
    font-size: 24px;
    margin-bottom: 20px;
}

form {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

label {
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 5px;
}



#propertyType option,
#location option {
    font-size: 16px;
    padding: 5px;

}

#propertyType option:nth-child(odd),
#location option:nth-child(odd) {
    background-color: rgb(242, 234, 234);
}

#dob {
    font-size: 20px;
    padding: 5px;
}

.radio {
    display: flex;
    margin-right: 20px;
}

input[type="text"],
input[type="email"],
input[type="password"],
textarea,
select {
    width: 97%;
    padding: 8px;
    border-radius: 5px;
    border: 1px solid #ccc;

}

input[type="radio"],
input[type="checkbox"] {
    margin-right: 5px;
}

button[type="submit"] {
    padding: 8px 16px;
    background-color: #4caf50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;

    margin: 20px auto;

    font-size: 20px;
}

button[type="submit"]:hover {
    background-color: #45a049;

}
</style>
  