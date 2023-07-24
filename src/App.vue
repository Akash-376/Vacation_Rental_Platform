<template>
  <div>
    <div id="nav">
      <div class="nav-logo">
        <img alt="Vue logo" src="./assets/logo.png">
        <h1>HOMES</h1>
      </div>
      <div v-if="role == 'guest'"  class="nav-link"> Guest: <span id="name">{{ name }}</span></div>
      <div v-if="role == 'host'"  class="nav-link"> Host: <span id="name">{{ name }}</span></div>
      <div class="nav-links">
        <!-- <router-link id="name" class="nav-link">{{name }}</router-link> -->
        <router-link class="nav-link" to="/">Properties</router-link>
        <router-link v-if="role == ''" class="nav-link" to="/homes/about">About us</router-link>
        <router-link v-if="role == 'host'" class="nav-link" to="/addProperty">Add Property</router-link>
        <router-link v-if="role == 'host'" class="nav-link" to="/hosts/myProperties">My Properties</router-link>
        <router-link v-if="role == 'guest'" class="nav-link" to="/guests/mybooking">My Bookings</router-link>
        <router-link v-if="role == ''" class="nav-link" to="/login">Login</router-link>
        <router-link v-if="role == 'guest' || role == 'host'" class="nav-link" to="/logout">Logout</router-link>
        <router-link v-if="role == ''" class="nav-link" to="/registerguest">Guest Signup</router-link>
        <router-link v-if="role == ''" class="nav-link" to="/registerhost">Host Signup</router-link>
      </div>
    </div>
    <router-view />
    <FooterComp />
  </div>
</template>


<script>
import axios from 'axios';
import FooterComp from './components/Footre.vue'
export default {
  name: 'App',
  data() {
    return {
      role: '',
      name: '',
      baseUrl: 'https://vacation-rental-backend-ten.vercel.app/'

    };

  },
  components: {
    FooterComp
  },
  methods: {
    async getRole() {
      const credentials = JSON.parse(localStorage.getItem('credentials'));
      if (credentials) {
        this.role = credentials['role']
        if (this.role == 'host') {
          await axios.get(this.baseUrl+'hostnamebyemail/' + credentials['email'])  // endpoint changed because fetching whole document of host was throwing CORS error
          .then(response => {
            this.name = response.data;
          })
          
        } else {
          await axios.get(this.baseUrl+'guestbyemail/' + credentials['email'])
            .then(response => {
              this.name = response.data.name;
            })
        }

      }
    }
  },
  mounted() {
    this.getRole()
  }


}
</script>

<style scoped>

#nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  padding: 5px;
  color: #fff;
  width: 99.3%;
  position: sticky;
  top: 0;
  z-index: 2;
}

.nav-logo {
  display: flex;
  text-align: center;
  justify-content: space-between;
  align-items: center;
  margin-left: 30px;
}

.nav-logo h1 {
  margin: 0;
  padding: 0;
  margin-left: 10px;
}

.nav-logo img {
  height: 40px;
  width: auto;

}

.nav-links {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 20px;
  padding-right: 30px;
}

.nav-link {
  color: #fff;
  text-decoration: none;
  padding: 10px;
  margin-left: 20px;
  font-size: 20px;
}

.nav-link:hover {
  background-color: #555;
}

.nav-link.router-link-exact-active {
  background-color: #777;
}

.login-btn {
  background-color: #555;
  padding: 10px 20px;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* Position the login button on the right corner */
.nav-links .login-btn {
  margin-left: auto;
}

#name {
  background: linear-gradient(90deg, red, orange, teal, yellow, red);
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
}
</style>
