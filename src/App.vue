<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <HostComp msg="Welcome Host"/> -->
  <div id="nav">
    <router-link class="nav" to="/registerhost">Register host</router-link>
    <router-link class="nav" to="/addProperty">Add Property</router-link>
    <router-link class="nav" to="/">Properties</router-link>
    <router-link class="nav" to="/login">Login</router-link>
    <router-link class="nav" to="/logout">Logout</router-link>
  </div>
  <router-view />
</template>

<script>
export default {
  name: 'App',
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  #nav{
    display: flex;
    background-color: #3498DB;
  }
  .nav {
    color: rgb(47, 45, 45);
    font-weight: bold;
    display: flex;
    text-decoration: none;
    margin: 20px;
    font-size: 20px;
    
    /* Add other styles as needed */
  }
  .nav:hover{
    color: #D35400 ;
  }
  
}
</style>
