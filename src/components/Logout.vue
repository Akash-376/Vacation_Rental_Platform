<template>
    <h1></h1>
</template>
<script>
import Swal from 'sweetalert2';
export default {
    name: 'LogoutComp',

    methods: {
        // Logout Method
        logout() {
            // Remove credentials from localStorage
            localStorage.removeItem('credentials');

            Swal.fire({
                title: 'Success!',
                text: 'Logged out Successfully !',
                icon: 'success',
                showConfirmButton: false, // Remove the 'OK' button
                timer: 2500, // Set the timer for 2 seconds (adjust as needed)
                willClose: () => {
                    window.location = '/'; // Redirect after the animation completes
                }
            });

            // Optionally, you can redirect to the login page or perform any other desired action
            // window.location = '/';
        }
    },
    created() {
        this.logout();
    }

}

</script>
<style scoped>
h1 {
    text-align: center;
    margin-top: 200px;
}
</style>