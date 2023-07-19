<template>
    <h1>Logging out...</h1>
</template>
<script>
    export default {
        name: 'LogoutComp',

        methods: {
            // Logout Method
            logout() {
                // Remove credentials from localStorage
                localStorage.removeItem('credentials');

                // Optionally, you can redirect to the login page or perform any other desired action
                window.location = '/login';
            }
        },
        created(){
            this.logout();
        }
        
    }

</script>
<style scoped>
    h1{
        text-align: center;
        margin-top: 200px;
    }
</style>