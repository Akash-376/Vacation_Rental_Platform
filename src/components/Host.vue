<template>
    <div id="body">


        <div id="container">
            <h1>Register Host</h1>
            <form @submit.prevent="registerHost">
                <label for="name">Name</label>
                <input type="text" id="name" v-model="hostData.name" required>

                <label for="mobile">Mobile</label>
                <input type="text" id="mobile" v-model="hostData.mobile" required>

                <label for="email">Email</label>
                <input type="email" id="email" v-model="hostData.email" required>

                <label for="password">Password</label>
                <input type="password" id="password" v-model="hostData.password" required>

                <label for="status">Status</label>
                <input type="status" id="status" v-model="hostData.status" readonly>


                <label for="gender">Gender</label>
                <div class="radio">

                    <div>
                        <input type="radio" id="male" value="Male" v-model="hostData.gender">
                        <label for="male">Male</label>
                    </div>
                    <div>
                        <input type="radio" id="female" value="Female" v-model="hostData.gender">
                        <label for="female">Female</label>
                    </div>

                </div>

                <!-- <input type="text" id="location" v-model="hostData.location" required> -->





                <label for="about">About</label>
                <textarea id="about" v-model="hostData.about" required></textarea>

                <label for="hostingSince">Hosting Since</label>
                <input type="date" id="hostingSince" v-model="hostData.hosting_since" :max="getCurrentDate()" required>

                <button type="submit">Register</button>
            </form>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios'
import Swal from 'sweetalert2';
export default {
    name: "HostComp",
    data() {
        return {
            hostData: {
                name: "",
                mobile: "",
                email: "",
                password: "",
                status: "Active",
                gender: "",
                about: "",
                hosting_since: ""
            }
        };
    },
    methods: {
        registerHost() {

            axios.post('http://localhost:5000/hosts', this.hostData)
                .then(response => {
                    // Handle the response from the server
                    // Optionally, you can display a success message or redirect to a different page
                    const hostId = response.data.host_id;

                    Swal.fire({
                        title: 'Host registered Successfully!',
                        text: "Host ID : " + hostId,
                        icon: 'success',
                        showConfirmButton: false, // Remove the 'OK' button
                        timer: 2500, // Set the timer for 2 seconds (adjust as needed)
                        willClose: () => {
                            window.location = '/login'; // Redirect after the animation completes
                        }
                    });



                    // alert("Added! with host ID "+ hostId)
                    // window.location = '/'
                })
                .catch(error => {
                    // Handle any errors that occurred during the registration process
                    // Optionally, you can display an error message to the user

                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: error.response.data.error,
                        footer: '<a href="/">go to home page</a>'
                    })

                    // alert(error.response.data.error)
                });
        },
        getCurrentDate() {
            const today = new Date();
            const year = today.getFullYear();
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

#hostingSince {
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
  