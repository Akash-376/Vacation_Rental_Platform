<template>
    <div id="body">

        <div id="container">
            <h1>Login</h1>
            <form @submit.prevent="login">
                <label for="email">Email:</label>
                <input type="email" id="email" v-model="credentials.email" required>

                <label for="password">Password:</label>
                <input type="password" id="password" v-model="credentials.password" required>

                <label for="gender">Role:</label>
                <div class="radio">

                    <div>
                        <input type="radio" id="host" value="host" v-model="role">
                        <label for="host">Host</label>
                    </div>
                    <div>
                        <input type="radio" id="guest" value="guest" v-model="role">
                        <label for="guest">Guest</label>
                    </div>

                </div>

                <button type="submit">Login</button>
            </form>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios'
import Swal from 'sweetalert2'
export default {
    name: 'LoginComp',
    data() {
        return {
            credentials: {
                email: '',
                password: ''
            },
            role: ''
        };
    },
    methods: {
        login() {

            const endpoint = this.getEndpoint();
            axios.post(endpoint, this.credentials)
                .then(response => {
                    localStorage.setItem('credentials', JSON.stringify(response.data));
                    Swal.fire({
                        title: 'Success!',
                        text: 'Logged In Successfully !',
                        icon: 'success',
                        showConfirmButton: false, // Remove the 'OK' button
                        timer: 2000, // Set the timer for 2 seconds (adjust as needed)
                        willClose: () => {
                            window.location = '/'; // Redirect after the animation completes
                        }
                    });


                })
                .catch(error => {

                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: error.response.data.error,
                        confirmButtonText: 'Try again',
                        footer: '<a href="/">Go to home page</a>'
                    })

                    // alert("Error: " + error.response.data.error);
                });
        },
        getEndpoint() {
            return `http://localhost:5000/${this.role}/login`;
        },

    }
};
</script>

<style scoped>
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
    /* margin-bottom: 20px; */
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
    /* Center the button horizontally */
    margin: 20px auto;
    /* Optional: Center the button within its container */
    font-size: 20px;
}

button[type="submit"]:hover {
    background-color: #45a049;

}
</style>
  